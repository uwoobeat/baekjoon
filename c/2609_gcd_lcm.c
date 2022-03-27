//2609 S5 gcd_lcm

#include <stdio.h>
#define max(a, b) (a > b ? a : b) //preprocessor and macro function
 
int gcd(int a, int b)
{
    if (b == 0) return a;
    else return gcd(b, a % b);
}

int lcm_1(int a, int b) //brute force...?
{
    int result; //be careful of variable scope...!

    for (int i = max(a,b); 1; i++) 
    {
        if (i % a == 0 && i % b == 0)
        {
            result = i;
            break;
        }
    }
    return result;
}

int lcm_2(int a, int b) //using a * b = gcd(a,b) * lcm(a,b)
{
    return a * b / gcd(a, b);
}

int main()
{
    int x, y;
    scanf("%d %d", &x, &y);
    printf("%d\n", gcd(x, y));
    printf("%d\n", lcm_1(x, y));
    printf("%d\n", lcm_2(x, y));
}