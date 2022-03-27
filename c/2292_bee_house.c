#include <stdio.h>

int main()
{
    int N, count = 1, start = 1, end = 1;
    scanf("%d", &N);

    if (N != 1)
    {
        while (1)
        {
            start += 1;
            end += 6 * count;
            count += 1;
            if (N >= start && N <= end) break; 
        }
    }

    printf("%d", count);
}