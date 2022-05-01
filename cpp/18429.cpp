#include <bits/stdc++.h>
#define FASTIO ios::sync_with_stdio(false); cin.tie(0); cout.tie(0);
using namespace std;

int n, k, ans, weight = 500, arr[50];
bool visited[50] = {0,};
vector<int> v;

void solve() {
    if (v.size() == n) {
        ans++;
        return;
    }
    for (int i=0; i<n; i++) {
        if (accumulate(v.begin(), v.end(), 500) - v.size() * 5 < 500) continue;
        v.push_back(arr[i]);
        visited[i] = 1;
        solve();
        visited[i] = 0;
        v.pop_back();
    }
}

int main()
{
    FASTIO
    cin >> n >> k;
    for (int i=0; i<n; i++) cin >> arr[i];
    
    solve();

    cout << ans;

    return 0;
}

/*
vector 선언해주고, 계속 넣어준다.

0-3, 1-7, 3-5

for (0부터 2까지)
    

f
*/