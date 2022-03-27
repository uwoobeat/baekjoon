//1259 B1 palindrome

#include <stdio.h>
#include <string.h>

int main()
{
    char arr[5];
    int len, check;

    while (1)
    {
        scanf("%s", &arr);
        if (arr[0] == '0') break;

        check = 1;
        len = strlen(arr);

        for (int i = 0; i < len/2; i++)
        {
            if (!(arr[i] == arr[len-1-i])) check = 0;
        }
        
        if (check) printf("yes\n");
        else printf("no\n");
    }
}