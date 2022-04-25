#include <bits/stdc++.h>
#define FASTIO ios::sync_with_stdio(false); cin.tie(0); cout.tie(0);
using namespace std;

int n, m;
bool visited[9];
vector<int> v;

void solve() {
    if (v.size() == m) {
        for (auto &k : v) cout << k << ' ';
        cout << '\n';
        return;
    }

    for (int i=v.back()+1; i<=n; i++) {
        v.push_back(i);
        solve();
        v.pop_back();
    }
}

int main()
{
    FASTIO
    cin >> n >> m;
    
    for (int i=1; i<=n; i++) {
        v.push_back(i);
        solve();
        v.pop_back();
    }

    return 0;
}