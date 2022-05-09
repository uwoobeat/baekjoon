#include <bits/stdc++.h>
#define FASTIO ios::sync_with_stdio(false); cin.tie(0); cout.tie(0);
using namespace std;

int arr[1001];
int dp[1001];

int main()
{
    FASTIO

    int n, ans = 1; cin >> n;
    for (int i=0; i<n; i++) cin >> arr[i];

    dp[0] = 1;
    for (int i=1; i<n; i++) {
        dp[i] = 1; //디폴트 값은 1
        for (int j=0; j<i; j++) {
            if (arr[j] < arr[i]) dp[i] = max(dp[i], dp[j] + 1);
            //앞에 있는 것들 중 현재 위치보다 작으면 j의 dp테이블에서 +1 값과 비교 후 갱신 
        }
        ans = max(ans, dp[i]); //dp 결과값 확인함으로써 최댓값 갱신
    }

    cout << ans;

    return 0;
}