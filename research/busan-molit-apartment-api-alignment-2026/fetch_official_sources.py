#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""POOL-28: retrieve 2026-01..04 Busan JSON and MOLIT XML snapshots.

Python 3.9+, standard library only. Keys are prompted and never written.
Use --self-test --fixture-dir DIR to validate existing original ZIPs without network.
"""
import argparse
import datetime as datetime
import getpass
import hashlib
import json
import math
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
import zipfile
from pathlib import Path

CITY_URL = 'https://apis.data.go.kr/6260000/HouseTradePriceService/getHouseTradePrice'
MOLIT_URL = 'https://apis.data.go.kr/1613000/RTMSDataSvcAptTrade/getRTMSDataSvcAptTrade'
MONTHS = [f'2026{n:02d}' for n in range(1, 5)]
DISTRICTS = ('26110', '26230')
MAX_RESPONSE_BYTES = 10 * 1024 * 1024


def parse_json(data):
    obj = json.loads(data)
    response = obj['response']
    head = response['header']
    if str(head.get('resultCode', '')) not in ('0', '00', '000'):
        raise ValueError('City API application status not successful')
    body = response['body']
    total = int(body['totalCount'])
    items = body.get('items') or []
    if isinstance(items, dict):
        items = items.get('item') or []
    if isinstance(items, dict):
        items = [items]
    if total < 0 or not isinstance(items, list) or any(not isinstance(v, dict) for v in items):
        raise ValueError('Invalid City items/totalCount')
    return items, total


def parse_xml(data):
    root = ET.fromstring(data)
    head = root.find('.//header')
    if head is None:
        raise ValueError('Missing MOLIT response header')
    code = (head.findtext('resultCode') or '').strip()
    if code not in ('0', '00', '000'):
        raise ValueError('MOLIT API application status not successful')
    total_str = root.findtext('.//body/totalCount')
    if total_str is None:
        raise ValueError('Missing MOLIT totalCount')
    total = int(total_str)
    items = [{node.tag.lower(): (node.text or '').strip() for node in item}
             for item in root.findall('.//body/items/item')]
    if total < 0:
        raise ValueError('Invalid MOLIT totalCount')
    return items, total


def retrieve(url, params, key, timeout):
    q = dict(params)
    q['serviceKey'] = key
    req = urllib.request.Request(url + '?' + urllib.parse.urlencode(q),
                                 headers={'User-Agent': 'ARHRN-POOL28-Stage13/1.0'})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as response:
            if response.status != 200:
                raise RuntimeError('HTTP non-200')
            raw = response.read(MAX_RESPONSE_BYTES + 1)
    except urllib.error.HTTPError as e:
        raise RuntimeError('HTTP status ' + str(e.code)) from None
    except (urllib.error.URLError, TimeoutError):
        raise RuntimeError('Network error or timeout') from None
    if len(raw) > MAX_RESPONSE_BYTES:
        raise RuntimeError('Response size limit exceeded')
    return raw


def audit_page(root, source, month, district, page, size, raw, items, total, params):
    folder = f'BUSAN_{month}' + (f'_P{page}' if page > 1 else '') if source == 'BUSAN' else f'MOLIT_{district}_{month}' + (f'_P{page}' if page > 1 else '')
    path = root / folder
    path.mkdir(parents=True, exist_ok=True)
    sha = hashlib.sha256(raw).hexdigest()
    ext = '.json' if source == 'BUSAN' else '.xml'
    name = f'official_api_response_{sha[:12]}{ext}'
    (path / name).write_bytes(raw)
    audit = {
        'research': 'ARHRN-POOL28-BUSAN-MOLIT-API-ALIGNMENT-20261111',
        'captured_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'endpoint_path': urllib.parse.urlparse(CITY_URL if source == 'BUSAN' else MOLIT_URL).path,
        'non_secret_params': list(params.items()), 'source': source,
        'row_count': len(items), 'total_count': total, 'sha256': sha,
        'raw_file': folder + '/' + name, 'status': 'PASS'
    }
    (path / 'stage0_audit.json').write_text(json.dumps(audit, ensure_ascii=False, indent=2), encoding='utf-8')
    return audit


def collect_one(root, source, month, district, key, size, timeout, pause):
    url = CITY_URL if source == 'BUSAN' else MOLIT_URL
    expected = None
    seen = 0
    page = 1
    pages = []
    while True:
        if page > 100:
            raise RuntimeError('Page safety cap exceeded')
        params = ({'pageNo': str(page), 'numOfRows': str(size), 'resultType': 'json', 'hsTypeNm': '아파트', 'ctrtYm': month}
                  if source == 'BUSAN' else {'LAWD_CD': district, 'DEAL_YMD': month, 'numOfRows': str(size), 'pageNo': str(page)})
        raw = retrieve(url, params, key, timeout)
        items, total = parse_json(raw) if source == 'BUSAN' else parse_xml(raw)
        if expected is None:
            expected = total
        elif total != expected:
            raise RuntimeError('totalCount changed during pagination; abort snapshot')
        if len(items) > size or (seen < total and not items):
            raise RuntimeError('Page count invalid, incomplete, or unexpected empty page')
        for item in items:
            if source == 'BUSAN':
                if str(item.get('ctrtYm') or item.get('ctrtym') or '') != month or item.get('hsTypeNm') != '아파트':
                    raise RuntimeError('City row date/type filter mismatch')
            else:
                year = str(item.get('dealyear') or '')
                row_month = str(item.get('dealmonth') or '').zfill(2)
                if year + row_month != month or str(item.get('sggcd') or '') != district:
                    raise RuntimeError('MOLIT row date/district filter mismatch')
        seen += len(items)
        if seen > total:
            raise RuntimeError('Pagination returned more than totalCount')
        a = audit_page(root, source, month, district, page, size, raw, items, total, params)
        pages.append({'file': a['raw_file'], 'sha256': a['sha256'], 'rows': len(items)})
        print(f'{source} {district or "ALL"} {month} page={page}: {seen}/{total}', flush=True)
        if seen == total:
            break
        page += 1
        time.sleep(pause)
    return {'source': source, 'district': district, 'month': month,
            'count': seen, 'totalCount': expected, 'pages': pages}


def self_test(fixtures):
    names = ['POOL28_JUNGGU_202601_SOURCE_REVIEW.zip',
             'POOL28_202602_202604_SOURCE_REVIEW.zip',
             'POOL28_BUSANJINGU_MOLIT_4MONTH_RAW.zip']
    n = 0
    groups = set()
    for zn in names:
        with zipfile.ZipFile(fixtures / zn) as z:
            for filename in z.namelist():
                if 'official_api_response_' not in filename:
                    continue
                raw = z.read(filename)
                city = filename.endswith('.json')
                rows, total = parse_json(raw) if city else parse_xml(raw)
                assert len(rows) <= total, filename
                n += 1
                groups.add(filename.split('/')[0].split('_P')[0])
    assert n == 23, (n, 'expected 23 historical raw files')
    assert len(groups) == 12, (groups, 'expected 4 city + 8 MOLIT query groups')
    print(json.dumps({'historical_fixtures': n, 'query_groups': len(groups), 'parser_test': 'PASS'}, ensure_ascii=False))


def package_compatibility_zips(out):
    """Match the archived ZIP grouping consumed by reproduce_pool28.py."""
    specs = {
        'POOL28_JUNGGU_202601_SOURCE_REVIEW.zip': lambda d: d.startswith('BUSAN_202601') or d.startswith('MOLIT_26110_202601'),
        'POOL28_202602_202604_SOURCE_REVIEW.zip': lambda d: (d.startswith('BUSAN_202602') or d.startswith('BUSAN_202603') or d.startswith('BUSAN_202604') or d.startswith('MOLIT_26110_202602') or d.startswith('MOLIT_26110_202603') or d.startswith('MOLIT_26110_202604')),
        'POOL28_BUSANJINGU_MOLIT_4MONTH_RAW.zip': lambda d: d.startswith('MOLIT_26230_')
    }
    for zipname, match in specs.items():
        with zipfile.ZipFile(out/zipname, 'w', compression=zipfile.ZIP_DEFLATED) as archive:
            for folder in sorted(p for p in out.iterdir() if p.is_dir()):
                if match(folder.name):
                    for f in sorted(folder.iterdir()):
                        if f.is_file():
                            archive.write(f, f.relative_to(out).as_posix())
    return list(specs)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--out', default='POOL28_STAGE13_NEW_SNAPSHOT')
    ap.add_argument('--page-size', type=int, default=1000)
    ap.add_argument('--timeout', type=int, default=45)
    ap.add_argument('--pause', type=float, default=0.35)
    ap.add_argument('--self-test', action='store_true', help='No internet; validate 23 archived fixtures')
    ap.add_argument('--fixture-dir', default='.', help='Directory holding three archived source ZIP files')
    args = ap.parse_args()
    if args.self_test:
        self_test(Path(args.fixture_dir))
        return 0
    if not 1 <= args.page_size <= 1000 or args.timeout < 5 or args.pause < 0:
        ap.error('invalid page-size/timeout/pause')
    out = Path(args.out).resolve()
    if out.exists() and any(out.iterdir()):
        ap.error('output directory must be new or empty: ' + str(out))
    out.mkdir(parents=True, exist_ok=True)
    city_key = getpass.getpass('Busan City API key (hidden): ').strip()
    molit_key = getpass.getpass('MOLIT apartment sales API key (hidden): ').strip()
    if not city_key or not molit_key:
        ap.error('both API keys required')
    result = {'research':'POOL-28', 'captured_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(), 'status':'INCOMPLETE', 'queries':[],
              'note':'New snapshots need not match the historical Nov 2026 archive; compare separately.'}
    try:
        for month in MONTHS:
            result['queries'].append(collect_one(out, 'BUSAN', month, '', city_key, args.page_size, args.timeout, args.pause))
            time.sleep(args.pause)
        for district in DISTRICTS:
            for month in MONTHS:
                result['queries'].append(collect_one(out, 'MOLIT', month, district, molit_key, args.page_size, args.timeout, args.pause))
                time.sleep(args.pause)
        result['compatibility_zips'] = package_compatibility_zips(out)
        result['status'] = 'PASS'
    except (ValueError, RuntimeError, OSError, ET.ParseError, json.JSONDecodeError) as e:
        result['error'] = str(e)[:240]
        print('Collection stopped; safe error: '+str(e)[:240], file=sys.stderr)
    finally:
        (out/'STAGE13_COLLECTION_MANIFEST.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
        print('Manifest:', str(out/'STAGE13_COLLECTION_MANIFEST.json'))
    return 0 if result['status']=='PASS' else 2

if __name__ == '__main__':
    sys.exit(main())
