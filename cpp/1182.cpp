#include <bits/stdc++.h>
#define FASTIO ios::sync_with_stdio(false); cin.tie(0); cout.tie(0);
using namespace std;

int n, s, ans, arr[21];

void solve(int idx, int sum) {
    if (idx == n) return;
    if (arr[idx] + sum == s) ans++;

    solve(idx+1, sum+arr[idx]);
    solve(idx+1, sum);
}

int main()
{
    FASTIO
    cin >> n >> s;
    for (int i=0; i<n; i++) cin >> arr[i];

    solve(0,0);

    cout << ans;
    
    return 0;
}