# Nexon Cash Hunter 🕵️‍♂️💰

> 넥슨 캐시 어디까지 충전했는지 내 손으로 직접 확인!  
> 넥슨 캐시 기록, 내 지갑 사정을 모니터링 하는 착한(?) 프로그램입니다.
![2025-08-086 44 02-ezgif com-video-to-gif-converter](https://github.com/user-attachments/assets/dad495de-23d3-4981-bdde-6d7e16651e39)
![2025-08-086 51 47-ezgif com-video-to-gif-converter](https://github.com/user-attachments/assets/e3c940fe-74d8-45fe-ac16-436d6369702f)

---

## 뭐하는 녀석인가요?

넥슨에 현질을 단 한번이라도 해본 당신!  
내 넥슨 캐시 충전 내역을 싹~ 긁어오는 파이썬, 자바스크립트 스크립트입니다.

> “넥슨 캐시 충전 내역, 이젠 숨기지 마라!”  
> (넥슨아, 이거 해킹 아니에요. 그냥 내 정보 조회할 뿐!)

---

## 기능

- 크롬 브라우저에서 자동으로 NPP 쿠키 찾아냄  
- 넥슨 API에 쿼리 날려 월별 충전 금액 조회  
- 2017년부터 현재까지 충전 내역 쭉 보여줌  
- 총 충전 금액까지 계산해서 알려줌  

---

## 준비물

- Windows 또는 macOS에 설치된 Python 3.x 
- 크롬 브라우저에 넥슨 로그인 완료 상태  
- `browser-cookie3` & `requests` 라이브러리 (아래 설치 명령어 참고)
---

## 설치 방법

```bash
pip install browser-cookie3 requests
```

## 사용 방법
```bash
python nexon_cash_hunter_win.py
python nexon_cash_hunter_mac.py
```
- 크롬 브라우저에서 사용할 경우 nexon_cash_hunte.js의 내용을 복사하여 개발자모드 Console에 붙여넣으면 됩니다.
