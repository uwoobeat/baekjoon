#include <bits/stdc++.h>
#define FASTIO ios::sync_with_stdio(false); cin.tie(0); cout.tie(0);
using namespace std;

int main()
{
    FASTIO
    
    vector<int> v;
    int sum = 0; 
    int cnt = 1;

    for (int i=0; i<9; i++) {
        int tmp; cin >> tmp;
        v.push_back(tmp);
        sum += tmp;
    }

    sort(v.begin(), v.end());

    for (int i=0; i<8; i++)
        for (int j=i+1; j<9; j++) {
            if (sum - v[i] - v[j] == 100) {
                for (int k=0; k<9; k++) {
                    if (k != i && k != j)
                        cout << v[k] << '\n';
                }
                return 0;
            }
        }
    
    return 0;
}