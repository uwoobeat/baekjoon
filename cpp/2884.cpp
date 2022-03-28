#include <bits/stdc++.h>
#define FASTIO ios::sync_with_stdio(false); cin.tie(0); cout.tie(0);
using namespace std;

int main()
{
    FASTIO
    int h, m;
    cin >> h >> m;

    if (m >= 45) cout << h << ' ' << m-45;
    else {
        if (h == 0) cout << 23 << ' ' << m+15;
        else cout << h-1 << ' ' << m+15;
    }

    return 0;
}