//2920 B2 music

#include <stdio.h>

int main()
{
    int x = 1, y = 1, arr[8];

    for (int i = 0; i < 8; i++)
        scanf("%d", &arr[i]);
    
    for (int i = 0; i < 8; i++)
    {
        if (arr[i] != i+1)
        {
            x = 0;
            break;
        }
    }

    for (int i = 0; i < 8; i++)
    {
        if (arr[i] != 8-i)
        {
            y = 0;
            break;
        }
    }

    if (!x && !y) printf("mixed\n");
    else if (x) printf("ascending\n");
    else if (y) printf("descending\n");
}

//등차수열의 감각으로 풀면 틀리는듯... 1~8, 8~1 수열의 일치로 판단하자.