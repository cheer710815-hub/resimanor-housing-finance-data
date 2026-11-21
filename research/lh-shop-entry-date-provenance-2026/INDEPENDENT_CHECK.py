#!/usr/bin/env python3
# Separate, independently coded minimal reproduction check (stdlib only)
import csv, hashlib, json, re, sys
from collections import defaultdict
from pathlib import Path

EXPECTED = (
    ('한국토지주택공사_상가 입찰 공고 내역_20201231.csv','cb3d3c0fbd33ee3ac5c581729996a4964766dd874bbc3e2e52a888069d6bf702'),
    ('한국토지주택공사_상가 공급 및 대금납부정보_20250827.csv','4fc36e8ff8900e2619adba940537eb935eebc6b04bd0c18e900a44052e99d92c'),
)
FIELDS=('사업지구','블록','상가명','호','전용면적')
def fetch(base,name,h):
    p=base/name
    digest=hashlib.sha256(p.read_bytes()).hexdigest()
    if digest!=h: raise ValueError(f'SHA256 mismatch for {name}')
    with p.open(encoding='cp949',newline='') as f:return list(csv.DictReader(f))
def main(base):
    data=[fetch(base,*info) for info in EXPECTED]
    groups=[]
    for rows in data:
        grouped=defaultdict(list)
        for rec in rows:
            k=tuple(rec[f].strip() for f in FIELDS)
            grouped[k].append(rec)
        repeated=[records for records in grouped.values() if len({(r['공고명'],r['공고게시일']) for r in records})>1]
        print('rows',len(rows),'unique shop combinations',len(grouped),'repeated combinations',len(repeated),'date changes within repeated',sum(len({v['입점시기'] for v in sub})>1 for sub in repeated))
        groups.append(grouped)
    x,y=groups; shared=x.keys()&y.keys()
    counts={'matched':len(shared),'same':0,'different':0,'missing':0}
    for k in shared:
        xs={r['입점시기'] for r in x[k]};ys={r['입점시기'] for r in y[k]}
        old=next(iter(xs)) if len(xs)==1 else ''
        new=next(iter(ys)) if len(ys)==1 else ''
        matched=re.fullmatch(r'2025-(\d{2})-(\d{2}) 00:00:00',new)
        a=old[:7] if re.fullmatch(r'\d{4}-\d{2}-\d{2}',old) else ''
        b=('20'+matched.group(2)+'-'+matched.group(1)) if matched else ''
        counts['missing' if not a or not b else 'same' if a==b else 'different']+=1
    assert counts=={'matched':1210,'same':1206,'different':1,'missing':3},counts
    print(json.dumps(counts,sort_keys=True))
if __name__=='__main__':
    try:main(Path(sys.argv[1]) if len(sys.argv)>1 else Path('.'))
    except Exception as e:print('INDEPENDENT_CHECK_FAILED:',e,file=sys.stderr);sys.exit(2)
