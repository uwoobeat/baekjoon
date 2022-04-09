#include <bits/stdc++.h>
#define FASTIO ios::sync_with_stdio(false); cin.tie(0); cout.tie(0);
using namespace std;

int arr[10000005];

int main()
{
    FASTIO
    int n;

    cin >> n;
    for (int i = 0; i < n; i++)
        cin >> arr[i];
    
    int min = *min_element(arr, arr+n);
    int max = *max_element(arr, arr+n);
    
    cout << min << ' ' << max;

    return 0;
}