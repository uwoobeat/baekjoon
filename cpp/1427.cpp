#include <bits/stdc++.h>
#define FASTIO ios::sync_with_stdio(false); cin.tie(0); cout.tie(0);
using namespace std;

int main()
{
    FASTIO;
    string n; cin >> n;

    sort(n.begin(), n.end(), [](int x, int y){return x>y;});
    
    cout << n;

    return 0;
}