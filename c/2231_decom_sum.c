//2231 B2 piece_sum

#include <stdio.h>

int get_piece_sum(int x)
{
    int sum = x;
    int temp = x;
    while (temp)
    {
        sum += temp % 10;
        temp /= 10;
    }
    return sum;
}

int main()
{
    int N, num = 1, check = 0;
    scanf("%d", &N);

    while (num < N)
    {
        if (get_piece_sum(num) == N)
        {
            check = 1;
            break;
        }
        num++;
    }

    if (check) printf("%d", num);
    else printf("0");
}