//2675 B2 string_repeat

#include <stdio.h>

int main()
{
    int T, R;
    char S[20];
    scanf("%d", &T);
    
    for (int i=0; i<T; i++)
    {
        scanf("%d %s", &R, S); 
        for (int j = 0; S[j]; j++)
            for (int k = 0; k < R; k++) printf("%c", S[j]);
        printf("\n");
    }
}