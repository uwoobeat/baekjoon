//2859 B1 sugar
/*
5로 채우고 그다음에 3 18 13 8 3
18인 경우 
16 11 5 3 0
16 11 6 1

5 나떨
5 나떨 x - 3 담기
*/

#include <stdio.h>

int main()
{
    int N, i, check = 1, bag = 0;
    scanf("%d", &N);
    i = N;

    while (1)
    {
        if (i % 5 == 0) 
        {
            bag += i / 5;
            printf("%d", bag);
            break;
        }
        else 
        {
            i -= 3;
            bag++;
        }

        if (i < 0)
        {
            printf("-1");
            break;
        }
    }
}