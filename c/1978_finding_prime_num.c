//1978 S4 finding_prime_num

#include <stdio.h>

int main()
{
    int N, count = 0;
    scanf("%d", &N);
    int arr[N];
    for (int i=0; i<N; i++) scanf("%d", &arr[i]);
    
    for (int i=0; i<N; i++)
    {
        if (arr[i] != 1)
        {
            int check = 0;
            for (int j=2; j < arr[i]; j++)
            {
                if (arr[i] % j == 0) check += 1;
            }
            if (!(check)) count += 1;
        }
    }

    printf("%d", count);
}