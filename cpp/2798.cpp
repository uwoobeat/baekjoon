#include <bits/stdc++.h>
#define FASTIO ios::sync_with_stdio(false); cin.tie(0); cout.tie(0);
using namespace std;

vector<int> v;

int main()
{
    FASTIO
    int n, m, ans = 0;

    cin >> n >> m;
    for (int i=0; i<n; i++) {
        int num; cin >> num;
        v.push_back(num);
    }

    for (int i=0; i<n; i++)
        for (int j=i+1; j<n; j++)
            for (int k=j+1; k<n; k++)
                if ((v[i]+v[j]+v[k] >= ans) && (v[i]+v[j]+v[k] <= m)) 
                    ans = v[i]+v[j]+v[k];
    cout << ans;

    return 0;
}