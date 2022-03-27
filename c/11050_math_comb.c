//11050 B1 math_comb

#include <stdio.h>

int factorial(int a)
{
    int temp = 1;
    for (int i = 1; i <= a; i++) temp *= i;
    return temp;
}

int main()
{
    int N, K;
    scanf("%d %d", &N, &K);
    printf("%d", factorial(N) / (factorial(K) * factorial(N-K)));
}

//binomail coefficient means number of combination in binomail fomula
//will be printed in integer