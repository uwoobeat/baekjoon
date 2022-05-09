#include <bits/stdc++.h>
#define FASTIO ios::sync_with_stdio(false); cin.tie(0); cout.tie(0);
using namespace std;

int dp[1000001];

int main()
{
    FASTIO
    
    int n; cin >> n;
    dp[1] = 0;
    for (int i=2; i<=n; i++) {
        dp[i] = dp[i-1] + 1;
        if (i%3 == 0) dp[i] = min(dp[i], dp[i/3] + 1);
        if (i%2 == 0) dp[i] = min(dp[i], dp[i/2] + 1);
    }

    cout << dp[n];

    return 0;
}

/*

dp 문제는 다음과 같이 풀이한다.

1. DP 테이블 정의
2. 점화식 찾기 (== 규칙성 발견)
3. 초깃값 설정


1. 탑다운 방식
- solve(x)에서 x==1이면 0, 기존재하는 값이면 dp테이블에서 찾아 반환한다.
- 아니라면 3번 케이스인 result = solve(x-1) + 1로 재귀호출된다.
- result 값을 받으면 해당 값을 dp에 저장한다.
- 1번, 2번 케이스에 해당하는지 확인 후 3번 케이스와 비교하여 결과값을 결정한다.
- 결과를 dp 테이블에 저장한다.

2. 바텀업 방식
- n에 도달할 때까지 dp 테이블을 채워가며 값을 구해간다.
- dp[i] = dp[i-1]+1로 하고, 1/2 조건 충족한다면 3으로 구한 값과 비교하여 갱신해준다.
*/