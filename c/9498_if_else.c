//9498 B4 if_else

#include <stdio.h>

int main()
{
    int score;
    char result;
    
    scanf("%d", &score);

    if (score >= 90) result = 'A';
    else if (score >= 80) result = 'B';
    else if (score >= 70) result = 'C';
    else if (score >= 60) result = 'D';
    else result = 'F';

    printf("%c", result);
}