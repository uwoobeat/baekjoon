// 2577 B2 num count

#include <stdio.h>

int main()
{
    int A, B, C, prod, arr[10] = {0,};
    scanf("%d %d %d", &A, &B, &C);
    prod = A * B * C;

    while (prod)
    {
        arr[prod % 10] += 1;
        prod /= 10;
    }

    for (int i = 0; i < 10; i++)
    {
        printf("%d\n", arr[i]);
    }
}