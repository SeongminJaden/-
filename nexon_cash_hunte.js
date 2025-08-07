(async () => {
  const nppCookie = document.cookie
    .split('; ')
    .find(row => row.startsWith('NPP='))
    ?.split('=')[1];

  if (!nppCookie) {
    console.error('NPP 쿠키를 찾지 못했습니다. 로그인 상태인지 확인하세요.');
    return;
  }

  const url = 'https://public.api.nexon.com/billing-bff/mycash';

  // 년도, 월 범위 설정 (Python 예제와 동일)
  const startYear = 2017;
  const endYear = 2025;

  let totalAmount = 0;

  // GraphQL 쿼리문
  const query = `
    query getNxCashHistoryCharge($year: Int!, $month: Int!) {
      nexonCashHistoryCharge(year: $year, month: $month) {
        chargeList {
          chargedAmount
          chargedCount
          paymentMethod
        }
      }
    }
  `;

  for (let year = startYear; year <= endYear; year++) {
    for (let month = 1; month <= 12; month++) {
      const payload = {
        query,
        variables: { year, month },
        operationName: 'getNxCashHistoryCharge'
      };

      try {
        const res = await fetch(url, {
          method: 'POST',
          headers: {
            'accept': 'application/graphql-response+json, application/json',
            'content-type': 'application/json',
            'origin': 'https://payment.nexon.com',
            'referer': 'https://payment.nexon.com/',
            'user-agent': navigator.userAgent,
            'cookie': `NPP=${nppCookie}`
          },
          body: JSON.stringify(payload),
          credentials: 'include'
        });

        if (!res.ok) {
          console.warn(`${year}년 ${month}월 조회 실패: ${res.status} ${res.statusText}`);
          continue;
        }

        const data = await res.json();

        const charges = data?.data?.nexonCashHistoryCharge?.chargeList;
        if (charges && charges.length > 0) {
          const monthSum = charges.reduce((acc, cur) => acc + parseInt(cur.chargedAmount, 10), 0);
          totalAmount += monthSum;
          console.log(`${year}년 ${month}월 총 충전 금액: ${monthSum}원`);
        } else {
          console.log(`${year}년 ${month}월 데이터 없음 또는 조회 실패`);
        }
      } catch (e) {
        console.error(`${year}년 ${month}월 요청 중 에러 발생:`, e);
      }
    }
  }

  console.log(`총 넥슨 충전 금액: ${totalAmount}원`);
})();
