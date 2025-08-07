import browser_cookie3
import requests
import json

def get_npp_cookie():
    cj = browser_cookie3.chrome(domain_name='.nexon.com')
    for cookie in cj:
        if cookie.name == "NPP":
            return cookie.value
    return None

def get_nexon_cash_history(year, month, npp_cookie):
    url = "https://public.api.nexon.com/billing-bff/mycash"

    headers = {
        "accept": "application/graphql-response+json, application/json",
        "content-type": "application/json",
        "origin": "https://payment.nexon.com",
        "referer": "https://payment.nexon.com/",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/138.0.0.0 Safari/537.36",
        "Cookie": f"NPP={npp_cookie}"
    }

    payload = {
        "query": """
          query getNxCashHistoryCharge($year: Int!, $month: Int!) {
            nexonCashHistoryCharge(year: $year, month: $month) {
              chargeList {
                chargedAmount
                chargedCount
                paymentMethod
              }
            }
          }
        """,
        "variables": {
            "year": year,
            "month": month
        },
        "operationName": "getNxCashHistoryCharge"
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code} {response.reason}")
        print(response.text)
        return None

if __name__ == "__main__":
    npp_cookie = get_npp_cookie()
    if not npp_cookie:
        print("크롬 브라우저에서 NPP 쿠키를 찾지 못했습니다. 크롬 실행 상태와 로그인 상태를 확인하세요.")
        exit(1)

    total_amount = 0
    for year in range(2015, 2026):
        for month in range(1, 13):
            data = get_nexon_cash_history(year, month, npp_cookie)
            if data and data.get("data") and data["data"].get("nexonCashHistoryCharge") and data["data"]["nexonCashHistoryCharge"].get("chargeList"):
                charges = data["data"]["nexonCashHistoryCharge"]["chargeList"]
                if charges:
                    month_sum = sum(int(c["chargedAmount"]) for c in charges)
                    total_amount += month_sum
                    print(f"{year}년 {month}월 총 충전 금액: {month_sum}원")
                else:
                    print(f"{year}년 {month}월 데이터 없음 또는 조회 실패")
            else:
                print(f"{year}년 {month}월 데이터 없음 또는 조회 실패")

    print(f"총 넥슨 충전 금액: {total_amount}원")
