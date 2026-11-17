import zipfile,json,hashlib,re,xml.etree.ElementTree as ET,csv
from collections import Counter,defaultdict
from decimal import Decimal,InvalidOperation
from pathlib import Path
ROOT=Path(__file__).parent
ZIPS=['POOL28_JUNGGU_202601_SOURCE_REVIEW.zip','POOL28_202602_202604_SOURCE_REVIEW.zip','POOL28_BUSANJINGU_MOLIT_4MONTH_RAW.zip']
files={};audits={}
for zn in ZIPS:
  with zipfile.ZipFile(ROOT/zn) as z:
    for name in z.namelist():
      if name.endswith('.json') and name.endswith('stage0_audit.json'): audits[name]=json.loads(z.read(name))
      elif 'official_api_response_' in name and name.endswith(('.json','.xml')):
        b=z.read(name)
        if name in files and files[name]!=b: raise RuntimeError('conflicting raw '+name)
        files[name]=b
assert len(files)>=12,(len(files),'insufficient source files')
rows={'BUSAN':defaultdict(list),'MOLIT':defaultdict(list)};checks=[]
for name,b in files.items():
 folder=name.split('/')[0];month=re.search(r'20260[1-4]',folder).group(); district='JUNGGU' if folder.startswith('MOLIT_26110') else 'BUSANJINGU' if folder.startswith('MOLIT_26230') else None
 audit=audits.get(folder+'/stage0_audit.json')
 sha=hashlib.sha256(b).hexdigest()
 if audit and sha!=audit.get('sha256'):raise RuntimeError('SHA mismatch '+name)
 if name.endswith('.json'):
  obj=json.loads(b)['response']; items=obj['body']['items']; rr=items.get('item',[]) if isinstance(items,dict) else items
  if isinstance(rr,dict):rr=[rr]
  for r in rr:
   reg=str(r.get('sggNm',''))
   if reg.startswith('부산광역시 중구 '): rows['BUSAN'][('JUNGGU',month)].append(r)
   elif reg.startswith('부산광역시 부산진구 '): rows['BUSAN'][('BUSANJINGU',month)].append(r)
 else:
  root=ET.fromstring(b); rr=[{c.tag.lower():(c.text or '').strip() for c in item} for item in root.findall('.//item')]
  rows['MOLIT'][(district,month)]+=rr
 checks.append({'raw':name,'sha256':sha,'sha_audit_match':bool(audit),'rows':len(rr)})
def ntext(s):return re.sub(r'[^0-9a-z가-힣]','',str(s or '').lower())
def nnum(s):
 try:return format(Decimal(str(s or '').replace(',','').strip()), 'f').rstrip('0').rstrip('.') if '.' in format(Decimal(str(s or '').replace(',','').strip()), 'f') else format(Decimal(str(s or '').replace(',','').strip()), 'f')
 except:return ''
def apt(s):return ntext(s)
def location(r,source):
 if source=='MOLIT':return (ntext(r.get('umdnm')),ntext(r.get('jibun')))
 return (ntext(str(r.get('sggNm','')).split(' ')[-1]),ntext(r.get('lnbr')))
def key(r,source,level):
 if source=='MOLIT':
  ym=str(r.get('dealyear'))+str(r.get('dealmonth')).zfill(2)
  day=nnum(r.get('dealday'));amount=nnum(r.get('dealamount'));area=nnum(r.get('excluusear'));floor=nnum(r.get('floor'));building=apt(r.get('aptnm'))
 else:
  ym=str(r.get('ctrtym') or r.get('ctrtYm'));day=nnum(r.get('ctrtDay'));amount=nnum(r.get('dlngAmt'));area=nnum(r.get('xuar'));floor=nnum(r.get('flr'));building=apt(r.get('bldgNm'))
 out=(ym,day,amount,area,floor)
 if level=='coarse':return out
 return out+(building,)+location(r,source)
report={'research':'POOL-28','stage':'Stage 6 sensitivity / source-side read-only audit','raw_files':len(files),'raw_sha256_checks':len(checks),'raw_all_sha_match':all(x['sha_audit_match'] for x in checks),'scopes':[],'limitations':['This uses archived local source responses; it does not verify the 2026-11-09 live recheck raw bytes.','An equal key multiset is not unique legal contract identification.','No causal attribution of three exceptions is possible without data-producer field definitions and record history.']}
exc=[]
for district in ['JUNGGU','BUSANJINGU']:
 for month in ['202601','202602','202603','202604']:
  b=rows['BUSAN'][(district,month)];m=rows['MOLIT'][(district,month)]
  out={'district':district,'month':month,'busan_rows':len(b),'molit_rows':len(m)}
  for level in ['coarse','strict']:
   bc=Counter(key(r,'BUSAN',level) for r in b);mc=Counter(key(r,'MOLIT',level) for r in m)
   left=mc-bc;right=bc-mc
   out[level+'_molit_only_excess']=sum(left.values());out[level+'_busan_only_excess']=sum(right.values())
   out[level+'_ambiguous_molit_rows']=sum(v for v in mc.values() if v>1)
   out[level+'_ambiguous_busan_rows']=sum(v for v in bc.values() if v>1)
   if level=='strict':
    for k,n in left.items():
     candidates=[r for r in m if key(r,'MOLIT','strict')==k]
     exc.append({'district':district,'month':month,'extra':n,'key':k,'molit_cdealtype':[r.get('cdealtype') for r in candidates], 'molit_cancel_dates':[r.get('cdealday') for r in candidates]})
  out['molit_cancel_marked_rows']=sum(str(r.get('cdealtype','')).strip().upper()=='O' for r in m)
  report['scopes'].append(out)
report['strict_excess_groups']=exc
(ROOT/'ARHRN_POOL28_STAGE6_SENSITIVITY_AUDIT.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
with (ROOT/'ARHRN_POOL28_STAGE6_MONTHLY_RESULTS.csv').open('w',encoding='utf-8-sig',newline='') as f:
 w=csv.DictWriter(f,fieldnames=list(report['scopes'][0]));w.writeheader();w.writerows(report['scopes'])
print(json.dumps({'raw_files':len(files),'raw_sha256_match':report['raw_all_sha_match'],'scopes':report['scopes'],'strict_exceptions':exc},ensure_ascii=False,indent=2))
