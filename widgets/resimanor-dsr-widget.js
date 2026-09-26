(function(){
  const root = document.querySelector('[data-resimanor-dsr-widget]') || document.getElementById('resimanor-dsr-widget');
  if(!root) return;
  const data={
    40000000:{none:279000000,regional:256000000,capital:200000000},
    50000000:{none:349000000,regional:320000000,capital:250000000},
    60000000:{none:419000000,regional:383000000,capital:301000000},
    70000000:{none:489000000,regional:447000000,capital:351000000},
    80000000:{none:559000000,regional:511000000,capital:401000000},
    100000000:{none:698000000,regional:639000000,capital:501000000}
  };
  const fmt=n=>Math.round(n/10000000)/10+'억원';
  root.innerHTML='<div class="rsw-card"><div class="rsw-title">2026 스트레스 DSR 한도 예시</div><label>연소득<select data-income><option value="40000000">4,000만원</option><option value="50000000">5,000만원</option><option value="60000000">6,000만원</option><option value="70000000">7,000만원</option><option value="80000000">8,000만원</option><option value="100000000">1억원</option></select></label><label>시나리오<select data-scenario><option value="none">스트레스 미적용 예시</option><option value="regional">지역 예시(심사금리 4.75%)</option><option value="capital">수도권 규제지역 예시(심사금리 7.0%)</option></select></label><div class="rsw-result"><span>예상 주담대 한도</span><strong data-limit></strong></div><div class="rsw-note">DSR 40%, 실제 금리 4.0%, 30년 원리금균등상환 기준의 비교 예시입니다. 실제 승인금액은 LTV, 기존부채, 금융회사 심사 등에 따라 달라질 수 있습니다.</div><a class="rsw-source" href="https://resimanor.com/housing-finance-dsr-data/" target="_blank" rel="noopener">Resimanor 스트레스 DSR 데이터센터에서 근거 보기</a></div>';
  const calc=()=>{const i=root.querySelector('[data-income]').value;const s=root.querySelector('[data-scenario]').value;root.querySelector('[data-limit]').textContent=fmt(data[i][s]);};
  root.addEventListener('change',calc); calc();
  if(!document.getElementById('rsw-style')){const st=document.createElement('style');st.id='rsw-style';st.textContent='.rsw-card{box-sizing:border-box;max-width:520px;padding:20px;border:1px solid #ddd;border-radius:16px;background:#fff;font-family:Arial,\"Noto Sans KR\",sans-serif;color:#222}.rsw-title{font-size:21px;font-weight:700;margin-bottom:16px}.rsw-card label{display:block;font-size:14px;font-weight:600;margin:12px 0}.rsw-card select{box-sizing:border-box;width:100%;margin-top:7px;padding:11px;border:1px solid #ccc;border-radius:10px;background:#fff;font-size:14px}.rsw-result{margin-top:18px;padding:16px;border-radius:12px;background:#f6f6f6;text-align:center}.rsw-result span{display:block;font-size:12px;color:#666;margin-bottom:6px}.rsw-result strong{font-size:30px}.rsw-note{margin:12px 0 10px;font-size:12px;line-height:1.5;color:#666}.rsw-source{font-size:12px;color:#333;text-decoration:underline}';document.head.appendChild(st);}
})();