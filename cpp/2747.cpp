#include <bits/stdc++.h>
#define FASTIO                   \
    ios::sync_with_stdio(false); \
    cin.tie(0);                  \
    cout.tie(0);
using namespace std;

int dp[46]; // n<=45이므로 46개 저장하는 dp 배열 선언

int fibo(int n)
{
    if (n == 0) return 0;
    if (n == 1) return 1;
    if (dp[n] != -1) return dp[n];
    else return dp[n] = fibo(n - 1) + fibo(n - 2); //점화식은 직접 써보면서 파악
    //재귀 호출을 사용한 top-down vs 반복문 사용한 bottom-up
    //top-down은 구조와 점화식 이해 쉽지만 재귀호출이라서 자원 많이 소모
    //bottom-up은 자원 적게 쓰지만 코드 이해 어려움
}

int main()
{
    FASTIO

    int n;
    cin >> n;
    fill(dp, dp + n + 1, -1); // dp+n+1까지면 dp+n까지만 초기화
    dp[0] = 0, dp[1] = 1;

    cout << fibo(n);

    return 0;
}