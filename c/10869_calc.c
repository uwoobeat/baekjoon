// 10869 B5 calc

#include <stdio.h>

int main()
{
    int A, B;
    scanf("%d %d", &A, &B);
    printf("%d\n", A+B);
    printf("%d\n", A-B);
    printf("%d\n", A*B);
    printf("%d\n", A/B); 
    //정수로 서식 지정자(format specifier: debug시 자주 등장하므로 알아두자) 설정 시 몫이 된다
    printf("%d\n", A%B);
}