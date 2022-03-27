#include <stdio.h>
#include <string.h>

int main()
{
    char str[1000000];
    int len, check = 0, tmp = 0, res, rescnt, cnt[26] = {0};

    scanf("%s", str);
    len = strlen(str);

    for (int i = 'a'; i <= 'z'; i++)
    {
        for (int j = 0; j < len; j++)
        {
            if (i == str[j]) cnt[i -'a']++;
        }
    }

    for (int i = 'A'; i <= 'Z'; i++)
    {
        for (int j = 0; j < len; j++)
        {
            if (i == str[j]) cnt[i -'A']++;
        }
    }

    for (int i = 0; i < 26; i++)
    {
        if (cnt[i] > tmp) {
            check = 0;
            res = i;
            tmp = cnt[i];
            continue;
        }
        else if (cnt[i] == tmp) check = 1;
    }

    if (check)
        printf("?\n");
    else
        printf("%c\n", res + 'A');
}