# Embed & reuse

Resimanor의 공개 차트와 데이터를 기사·블로그·가이드에 사용할 수 있습니다. 출처 링크는 canonical data page로 연결해 주세요.

## Chart embed

### Markdown

```markdown
[![2026 스트레스 DSR 연소득별 주담대 한도 예시](https://raw.githubusercontent.com/cheer710815-hub/resimanor-housing-finance-data/main/assets/resimanor-dsr-income-chart.svg)](https://resimanor.com/housing-finance-dsr-data/)
```

### HTML

```html
<a href="https://resimanor.com/housing-finance-dsr-data/" target="_blank" rel="noopener">
  <img src="https://raw.githubusercontent.com/cheer710815-hub/resimanor-housing-finance-data/main/assets/resimanor-dsr-income-chart.svg"
       alt="2026 스트레스 DSR 연소득별 주담대 한도 예시"
       style="max-width:100%;height:auto;">
</a>
<p>자료: <a href="https://resimanor.com/housing-finance-dsr-data/">Resimanor 2026 주택금융·DSR 데이터센터</a></p>
```

## One-line source link

### HTML

```html
<p>출처: <a href="https://resimanor.com/housing-finance-dsr-data/" target="_blank" rel="noopener">Resimanor 스트레스 DSR 데이터센터</a></p>
```

### Markdown

```markdown
출처: [Resimanor 스트레스 DSR 데이터센터](https://resimanor.com/housing-finance-dsr-data/)
```

## Suggested reuse blocks

### DSR 데이터센터 링크

```html
<a href="https://resimanor.com/housing-finance-dsr-data/" target="_blank" rel="noopener">2026 스트레스 DSR 데이터센터</a>
```

## CSV links

- 연소득별 한도: https://raw.githubusercontent.com/cheer710815-hub/resimanor-housing-finance-data/main/income_mortgage_limits.csv
- 신용대출 잔액별 한도: https://raw.githubusercontent.com/cheer710815-hub/resimanor-housing-finance-data/main/credit_debt_mortgage_limits.csv

## License

CC BY 4.0. 재사용 시 출처와 원문 링크를 함께 표시해 주세요.


## Interactive widget

스트레스 DSR 한도 예시 위젯을 외부 블로그·교육자료·가이드에 삽입할 수 있습니다. 위젯 하단의 Resimanor 원문 링크를 유지해 주세요.

### HTML embed

```html
<div data-resimanor-dsr-widget></div>
<script src="https://cdn.jsdelivr.net/gh/cheer710815-hub/resimanor-housing-finance-data@main/widgets/resimanor-dsr-widget.js"></script>
```

### Widget source

- https://github.com/cheer710815-hub/resimanor-housing-finance-data/blob/main/widgets/resimanor-dsr-widget.js

### Canonical source

- https://resimanor.com/housing-finance-dsr-data/
