#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""POOL-47 Stage8: immutable official-source reproducibility and repeated-asset temporal provenance.
Python 3.9+ standard-library only. No internet, no changes to original CSVs.
This is an audit of recorded values; it never establishes physical occupancy dates.
"""
from __future__ import annotations
import argparse,csv,hashlib,json,re,sys
from collections import defaultdict,Counter
from decimal import Decimal,InvalidOperation
from pathlib import Path

RESEARCH_ID='ARHRN-LH-SHOP-PAYMENT-TERMS-GRAIN-QA-20261115'
EXPECTED={
 2020: ('cb3d3c0fbd33ee3ac5c581729996a4964766dd874bbc3e2e52a888069d6bf702',2545,29),
 2025: ('4fc36e8ff8900e2619adba940537eb935eebc6b04bd0c18e900a44052e99d92c',5763,34),
}
ASSET_COLS=('사업지구','블록','상가명','호','전용면적')
NOTICE_COLS=('공고명','공고게시일','상가명','호','전용면적')

def sha256(path):
 h=hashlib.sha256()
 with open(path,'rb') as f:
  for block in iter(lambda:f.read(1<<20),b''):h.update(block)
 return h.hexdigest()

def clean(s):return re.sub(r'\s+','',str(s or '').strip()).casefold()

def number(s):
 try:return format(Decimal(str(s or '').strip().replace(',','')).normalize(),'f')
 except (InvalidOperation,ValueError):return clean(s)

def asset_key(rec,with_floor=False):
 key=tuple(number(rec[c]) if c=='전용면적' else clean(rec[c]) for c in ASSET_COLS)
 return key+(number(rec['층']),) if with_floor else key

def notice_key(rec):
 return tuple(number(rec[c]) if c=='전용면적' else clean(rec[c]) for c in NOTICE_COLS)

def ym20(s):
 m=re.fullmatch(r'(?:19|20)\d\d-(?:0[1-9]|1[0-2])-\d\d',str(s).strip())
 return s[:7] if m else ''

def candidate25(s):
 m=re.fullmatch(r'2025-(0[1-9]|1[0-2])-(\d\d) 00:00:00',str(s).strip())
 return '20'+m.group(2)+'-'+m.group(1) if m else ''

def read(path,year):
 expected_hash,expected_n,expected_cols=EXPECTED[year]
 actual=sha256(path)
 if actual!=expected_hash:raise ValueError('SOURCE_HASH_MISMATCH for '+str(path))
 with path.open(encoding='cp949',newline='') as f:
  r=csv.DictReader(f);fields=r.fieldnames;records=[]
  for lineno,rec in enumerate(r,2):
   if None in rec:raise ValueError('MALFORMED_INPUT at '+str(lineno))
   rec['_source_line']=str(lineno);records.append(rec)
 if len(records)!=expected_n or len(fields)!=expected_cols:raise ValueError('SOURCE_SCHEMA_MISMATCH')
 if any(k not in fields for k in set(ASSET_COLS+NOTICE_COLS+('입점시기','예정가격','계약체결종료일'))):raise ValueError('MISSING_EXPECTED_FIELD')
 return records,fields

def output_csv(path,columns,rows):
 with path.open('w',newline='',encoding='utf-8-sig') as f:
  writer=csv.writer(f,lineterminator='\n');writer.writerow(columns);writer.writerows(rows)

def output_json(path,obj):path.write_text(json.dumps(obj,ensure_ascii=False,indent=2,sort_keys=True)+'\n',encoding='utf-8')

def group_asset(records,keymaker=asset_key):
 groups=defaultdict(list)
 for r in records:groups[keymaker(r)].append(r)
 return groups

def asset_summary(groups,year,out):
 rows=[];recurrent=0;constant=0;changed=0;price_var=0;contract_var=0;ratio_var=0
 for key,records in sorted(groups.items()):
  notices={(r['공고명'],r['공고게시일']) for r in records}
  if len(notices)<2:continue
  recurrent+=1
  dates={r['입점시기'] for r in records}
  prices={number(r['예정가격']) for r in records}
  contracts={r['계약체결종료일'] for r in records}
  ratios={r['계약금비율(퍼센트)'] for r in records}
  if len(dates)==1:constant+=1
  else:changed+=1
  price_var+=len(prices)>1
  contract_var+=len(contracts)>1
  ratio_var+=len(ratios)>1
  rows.append([year,*key,len(records),len(notices),len(dates),len(prices),len(contracts),len(ratios),';'.join(sorted(dates)),int(len(dates)==1)])
 output_csv(out/f'repeated_assets_{year}.csv',['vintage','business_district','block','shop_name','unit','area','rows','distinct_notices','distinct_entry_raw_values','distinct_prices','distinct_contract_ends','distinct_downpayment_ratios','entry_raw_values','date_constant_across_notices'],rows)
 return {'asset_keys':len(groups),'multi_notice_asset_keys':recurrent,'constant_date_asset_keys':constant,'changed_date_asset_keys':changed,'multi_notice_price_changed':price_var,'multi_notice_contract_end_changed':contract_var,'multi_notice_downpayment_ratio_changed':ratio_var}

def cross_assets(old,new,out):
 records=[];stats=Counter();disagree=[]
 for key in sorted(set(old)&set(new)):
  a,b=old[key],new[key]
  x={r['입점시기'] for r in a};y={r['입점시기'] for r in b}
  d0=ym20(next(iter(x))) if len(x)==1 else ''
  d1=candidate25(next(iter(y))) if len(y)==1 else ''
  if not d0 or not d1:status='MISSING_DATE'
  elif d0==d1:status='CONCORDANT_YM'
  else:status='DISCORDANT_YM'
  stats[status]+=1
  row=[*key,len({(r['공고명'],r['공고게시일']) for r in a}),len({(r['공고명'],r['공고게시일']) for r in b}),len(a),len(b),';'.join(sorted(x)),';'.join(sorted(y)),d0,d1,status,';'.join(r['_source_line'] for r in a),';'.join(r['_source_line'] for r in b)]
  records.append(row)
  if status=='DISCORDANT_YM':disagree.append((key,a,b))
 output_csv(out/'asset_cross_vintage.csv',['business_district','block','shop_name','unit','area','notices_2020','notices_2025','rows_2020','rows_2025','old_entry_raw','new_entry_raw','old_ym','new_ym_candidate_ONLY','status','source_lines_2020','source_lines_2025'],records)
 assert len(records)==1210 and stats['CONCORDANT_YM']==1206 and stats['DISCORDANT_YM']==1 and stats['MISSING_DATE']==3
 return {'shared_asset_keys':len(records),'both_dates_valid':stats['CONCORDANT_YM']+stats['DISCORDANT_YM'],'same_year_month_assets':stats['CONCORDANT_YM'],'different_year_month_assets':stats['DISCORDANT_YM'],'missing_date_assets':stats['MISSING_DATE']},disagree

def cross_notices(old,new,out):
 idx0=defaultdict(list);idx1=defaultdict(list)
 for r in old:
  if 2016<=int(r['공고게시일'][:4])<=2020:idx0[notice_key(r)].append(r)
 for r in new:
  if 2016<=int(r['공고게시일'][:4])<=2020:idx1[notice_key(r)].append(r)
 common=sorted(set(idx0)&set(idx1));stats=Counter()
 rows=[]
 for k in common:
  aa=idx0[k];bb=idx1[k];v0={r['입점시기'] for r in aa};v1={r['입점시기'] for r in bb}
  m0=ym20(next(iter(v0))) if len(v0)==1 else '';m1=candidate25(next(iter(v1))) if len(v1)==1 else ''
  status='MISSING' if not m0 or not m1 else 'MATCH' if m0==m1 else 'DIFFER'
  stats[status]+=1
  rows.append([*k,len(aa),len(bb),m0,m1,status])
 assert len(common)==1825 and stats['MATCH']==1820 and stats['DIFFER']==2 and stats['MISSING']==3
 output_csv(out/'notice_cross_vintage_summary.csv',['notice_name','notice_date','shop_name','unit','area','rows_2020','rows_2025','old_ym','new_ym_candidate_ONLY','status'],rows)
 return {'shared_notice_shop_keys':len(common),'both_dates_valid':stats['MATCH']+stats['DIFFER'],'same_year_month_notice_keys':stats['MATCH'],'different_year_month_notice_keys':stats['DIFFER'],'missing_date_notice_keys':stats['MISSING']}

def trace_disagreement(disagree,out):
 assert len(disagree)==1
 key,older,newer=disagree[0]
 assert '엔트라리움' in key[2] and key[3]=='101'
 rows=[]
 for year,recs in [(2020,older),(2025,newer)]:
  for r in sorted(recs,key=lambda x:(x['공고게시일'],x['입찰신청접수개시일시'],x['_source_line'])):
   rows.append([year,r['_source_line'],r['공고게시일'],r['공고명'],r['상가명'],r['호'],r['전용면적'],r['입점시기'],ym20(r['입점시기']) if year==2020 else candidate25(r['입점시기']),r['예정가격'],r['계약체결종료일'],r['입찰신청접수개시일시']])
 output_csv(out/'entrarium_lineage.csv',['vintage','source_csv_line','notice_date','notice_name','shop_name','unit','area','entry_raw','entry_ym_candidate_only','listed_price','contract_end','bid_start'],rows)
 return {'shop_name':'엔트라리움','unit':'101','source_2020_rows':len(older),'source_2025_rows':len(newer),'source_2020_notice_dates':sorted({r['공고게시일'] for r in older}),'source_2025_notice_dates':sorted({r['공고게시일'] for r in newer}),'old_published_year_month':'2019-10','new_published_candidate_year_month':'2022-02','interpretation':'VERSION_DIFFERENCE_NOT_PROOF_OF_PHYSICAL_OCCUPANCY_OR_ETL_CAUSE'}

def audit(p20,p25,out):
 old,_=read(p20,2020);new,_=read(p25,2025)
 out.mkdir(parents=True,exist_ok=True)
 assets0=group_asset(old);assets1=group_asset(new)
 recap0=asset_summary(assets0,2020,out);recap1=asset_summary(assets1,2025,out)
 overlap,disagree=cross_assets(assets0,assets1,out)
 pernotice=cross_notices(old,new,out)
 lin=trace_disagreement(disagree,out)
 controls={}
 for year,records in [(2020,old),(2025,new)]:
  for variant,name in [(lambda x:asset_key(x,True),'with_floor'),(asset_key,'base_5field')]:
   groups=group_asset(records,variant)
   recurrent=[v for v in groups.values() if len({(r['공고명'],r['공고게시일']) for r in v})>=2]
   controls[f'{year}_{name}']={'repeated_keys':len(recurrent),'keys_with_date_changes':sum(len({r['입점시기'] for r in group})>1 for group in recurrent)}
 assert recap0['multi_notice_asset_keys']==381 and recap1['multi_notice_asset_keys']==476
 assert recap0['changed_date_asset_keys']==recap1['changed_date_asset_keys']==0
 assert recap0['multi_notice_price_changed']==107 and recap1['multi_notice_price_changed']==131
 assert recap0['multi_notice_contract_end_changed']==381 and recap1['multi_notice_contract_end_changed']==476
 summary={'research_id':RESEARCH_ID,'review_stage':'Stage8 2026-11-20','sources':{'2020':{'rows':len(old),'columns':29,'sha256':EXPECTED[2020][0]},'2025':{'rows':len(new),'columns':34,'sha256':EXPECTED[2025][0]}},'same_vintage_asset_constancy':{'2020':recap0,'2025':recap1},'between_vintage_by_asset':overlap,'between_vintage_by_notice':pernotice,'discordant_asset_trace':lin,'sensitivity_repeated_asset_keys':controls,'claims_NOT_allowed':['2025-MM-YY is definitely an ETL bug','Candidate YYYY-MM is the actual date of occupancy','Different official files are independent measurements of actual occupancy','Both mismatched notices imply two faulty physical shops','Public publication/DOI was performed'],'conclusion':'PUBLISH_REVIEW_READY_INTERNAL_NOT_APPROVED_FOR_EXTERNAL_RELEASE'}
 output_json(out/'stage8_summary.json',summary)
 output_csv(out/'source_integrity.csv',['vintage','rows','columns','encoding','sha256'],[[y,summary['sources'][str(y)]['rows'],summary['sources'][str(y)]['columns'],'cp949',summary['sources'][str(y)]['sha256']] for y in (2020,2025)])
 manifest={p.name:sha256(p) for p in sorted(out.iterdir()) if p.is_file()}
 output_json(out/'analysis_manifest_sha256.json',manifest)
 print(json.dumps({'status':'PASS','multi_notice':{'2020':recap0['multi_notice_asset_keys'],'2025':recap1['multi_notice_asset_keys']},'asset_cross':overlap,'notice_cross':pernotice},ensure_ascii=False,sort_keys=True))

if __name__=='__main__':
 p=argparse.ArgumentParser()
 p.add_argument('--old2020',type=Path,required=True)
 p.add_argument('--new2025',type=Path,required=True)
 p.add_argument('--out',type=Path,required=True)
 x=p.parse_args()
 try:audit(x.old2020,x.new2025,x.out)
 except Exception as e:
  print('STAGE8_FAILED: '+str(e),file=sys.stderr);sys.exit(2)
