//10809

#include <stdio.h>
#include <string.h>

int main()
{
    char arr[100];
    char abc[26];
    char *x = arr;
    char *y = abc;
    int k = 0;

    scanf("%s", arr);

    for (int i = 0; i < 26; i++) {
        *(y+i) = -1;
    }

    for (int i = 'a'; i <= 'z'; i++) {
        for (int j = 0; j < strlen(arr); j++) {
            if (*(x+j) == i) {
                 k = *(x+j) - 'a'; 
                 *(y+k) = j;
                 break;
            }
        }
    }

    for (int i = 0; i < 26; i++) {
        printf("%d", *(y+k));
    }
    return 0;
}