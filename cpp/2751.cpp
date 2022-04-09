#include <bits/stdc++.h>
#define FASTIO ios::sync_with_stdio(false); cin.tie(0); cout.tie(0);
using namespace std;

int main()
{
    FASTIO
    int n; cin >> n;
    vector<int> v;
    for(int i=0; i<n; i++) {
        int tmp; cin >> tmp;
        v.push_back(tmp);
    }

    sort(v.begin(), v.end());

    for (auto i : v)
        cout << i << '\n';

    return 0;
}