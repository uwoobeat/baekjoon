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
        /*
        string does not need '&' : string contains adress, not value
        other variables contains value(not address), so calling-by-reference with &(val) is needed
        */

        for (int j = 0; S[j]; j++) //or j < strlen(S) by string.h
        {
            for (int k = 0; k < R; k++)
                printf("%c", S[j]);
        }
        printf("\n");
    }
}

//Q. Why S[j] can work in for-loop condition in line 20?
//A. char in array returns 'true', but empty value returns 'false': works same as j < strlen(S)