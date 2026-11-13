#!/usr/bin/env python3
"""Reproduce an audit of Seoul apartment misc income records. Python stdlib only."""
import argparse, collections, csv, hashlib, json
from pathlib import Path

EXPECTED = {
    '2022': dict(rows=735394, unique_codes=2351, unique_names=2372,
                 categories=15, codes_with_multiple_names=28,
                 names_with_multiple_codes=7, colliding_name_date_category_keys=349,
                 negative_rows=3058, blank_or_nonnumeric=2,
                 sha256='c676b180bc507c2e2e70470c2176ef5ab0ff9aaef1dd2bd80de8ad1805f3aa5f'),
    '2023': dict(rows=719513, unique_codes=2358, unique_names=2375,
                 categories=15, codes_with_multiple_names=22,
                 names_with_multiple_codes=5, colliding_name_date_category_keys=207,
                 negative_rows=2777, blank_or_nonnumeric=10,
                 sha256='b4921ad52bd45ff74801874fe0a4434eeabe89dd591fe796325ff7f245a49db1'),
}
FIELDS = ['아파트명','아파트코드','비용명','년월일','금액']

def audit(path):
    digest = hashlib.sha256()
    with path.open('rb') as f:
        for block in iter(lambda:f.read(1024*1024),b''):digest.update(block)
    rows=neg=invalid=0
    codes=set(); names=set(); categories=set()
    code_names=collections.defaultdict(set); name_codes=collections.defaultdict(set)
    keys=collections.defaultdict(set)
    with path.open(encoding='cp949', newline='') as f:
        reader=csv.DictReader(f)
        if list(reader.fieldnames or []) != FIELDS:
            raise ValueError(f'Unexpected header: {reader.fieldnames}')
        for r in reader:
            rows+=1
            name,code,cat,day,amount=(r[k] for k in FIELDS)
            codes.add(code);names.add(name);categories.add(cat)
            code_names[code].add(name);name_codes[name].add(code)
            keys[(name,day,cat)].add(code)
            try:
                number=float(amount.replace(',','').strip())
                if number!=number or abs(number)==float('inf'): raise ValueError('nonfinite')
                if number<0:neg+=1
            except (ValueError,TypeError):invalid+=1
    collisions=sum(len(v)>1 for v in keys.values())
    return dict(rows=rows, unique_codes=len(codes), unique_names=len(names),
                categories=len(categories),
                codes_with_multiple_names=sum(len(v)>1 for v in code_names.values()),
                names_with_multiple_codes=sum(len(v)>1 for v in name_codes.values()),
                colliding_name_date_category_keys=collisions,
                negative_rows=neg, blank_or_nonnumeric=invalid,
                sha256=digest.hexdigest()), codes

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--source-dir',type=Path,required=True,help='Directory containing original etc_income_2022.csv and etc_income_2023.csv')
    p.add_argument('--output',type=Path,default=Path('audit_results.json'))
    p.add_argument('--strict',action='store_true',help='Fail if results do not match audited originals')
    a=p.parse_args(); data={}; code_sets={}
    for year in ('2022','2023'):
        path=a.source_dir / f'etc_income_{year}.csv'
        if not path.is_file():p.error(f'Missing {path}')
        data[year],code_sets[year]=audit(path)
    data['shared_apartment_codes']=len(code_sets['2022'] & code_sets['2023'])
    a.output.parent.mkdir(parents=True,exist_ok=True)
    a.output.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    mistakes=[]
    for year in ('2022','2023'):
        mistakes.extend(f'{year}.{key}: expected {value}, got {data[year].get(key)}'
            for key,value in EXPECTED[year].items() if data[year].get(key)!=value)
    if data['shared_apartment_codes']!=2309:mistakes.append(f"common codes expected 2309 got {data['shared_apartment_codes']}")
    print(json.dumps({'output':str(a.output),'matches_expected':not mistakes,'differences':mistakes},ensure_ascii=False,indent=2))
    if a.strict and mistakes:raise SystemExit(1)

if __name__=='__main__':main()
