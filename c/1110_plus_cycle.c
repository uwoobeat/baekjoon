//1110 B! plus_cycle

#include <stdio.h>

int main()
{
    int N, num1, num2, result, count;
    scanf("%d", &N);
    num1 = N;
    count = 0;

    while (1)
    {
        num2 = num1 / 10 + num1 % 10;
        result = num1 % 10 * 10 + num2 % 10;
        num1 = result;
        count += 1;
        if (result == N) break;
    }

    printf("%d", count);
}