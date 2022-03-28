#include <bits/stdc++.h>
#define FASTIO ios::sync_with_stdio(false); cin.tie(0); cout.tie(0);
using namespace std;

int main()
{
    FASTIO
    int a, b;
    cin >> a >> b;

    if (a > b) cout << ">";
    else if (a < b) cout << "<";
    else if (a == b) cout << "==";

    return 0;
}