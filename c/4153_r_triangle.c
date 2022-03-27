//4153 B3 r_triangle

#include <stdio.h>

int main()
{
    while (1)
    {
        int a, b, c, count = 0;
        scanf("%d %d %d", &a, &b, &c);
        if (a == 0 && b == 0 && c == 0) break;
        
        if (a * a == b * b + c * c) count += 1;
        else if (b * b == a * a + c * c) count += 1;
        else if (c * c == a * a + b * b) count += 1;

        //케이스 누락 주의

        if (count) printf("right\n");
        else printf("wrong\n");
    }
}