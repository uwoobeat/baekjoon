#include <bits/stdc++.h>
#define FASTIO ios::sync_with_stdio(false); cin.tie(0); cout.tie(0);
using namespace std;

bool compare(string x, string y) {
    if (x.length() == y.length())
        return (x < y);
    else return (x.length() < y.length());
}

int main()
{
    FASTIO;
    int n; cin >> n;
    vector<string> v;
    for (int i=0; i<n; i++) {
        string tmp; cin >> tmp;
        v.push_back(tmp);
    }

    sort(v.begin(), v.end(), compare);
    v.erase(unique(v.begin(), v.end()), v.end()); //중복 제거 코드. 정렬 후 사용

    for (auto i : v) cout << i << '\n';

    return 0;
}