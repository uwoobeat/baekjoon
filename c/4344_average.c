//4344 B1 average

#include <stdio.h>

int main()
{
    int C;
    scanf("%d", &C);

    for (int i = 0; i < C; i++)
    {
        int N;
        double sum = 0, count = 0, average;
        scanf("%d", &N);
        int arr[N];
        for (int j = 0; j < N; j++)
        {
            scanf("%d", &arr[j]); 
        }

        for (int k = 0; k < N; k++)
        {
            sum += arr[k];
        }
        average = sum / N;

        for (int l = 0; l < N; l++)
        {
            if (arr[l] > average)
                count += 1;
        }
        printf("%.3f%%\n", count / N * 100);
    }
}