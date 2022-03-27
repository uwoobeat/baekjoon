#include <stdio.h>

int main() 
{
    int n, m, num, res = 0;
    scanf("%d %d", &n, &m);
    int arr[n];
    for (int i = 0; i < n; i++)
        scanf("%d", &arr[i]);

    for (int i = 1; i <= n-2; i++) {
        for (int j = i+1; j <= n-1; j++) {
            for (int k = j+1; k <= n; k++) {
                num = arr[i-1]+arr[j-1]+arr[k-1];
                if (num > res && num <= m) res = num;
            }
        }
    }

    printf("%d", res);
}