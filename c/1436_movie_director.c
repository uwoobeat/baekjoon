//1436 S5 movie_director

/*
1. 667d
*/
#include <stdio.h>

int main()
{
    int N, num = 666, count = 1;
    scanf("%d", &N);

    while (count != N)
    {
        num++;
        int i = num;
        while (i != 0)
        {
            if (i % 1000 == 666)
            {
                count++;
                break;
            }
            else i /= 10;
        }
    }
    printf("%d", num);
}