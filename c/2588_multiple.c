// 2588 B4 multiple

#include <stdio.h>

int main()
{
    int a,b;
    scanf("%d\n%d", &a, &b);
    /*
    파이썬의 input()은 개행 문자를 입력받지 못한다.
    따라서 두 줄을 입력받으려면 [input() for _ in range(2)]와 같이
    list comprehension을 이용해야 한다. 하지만 C는 개행 문자 역시 인식하므로,
    여러 줄의 입력도 한 번에 받을 수 있는듯?
    */
    printf("%d\n", a * (b % 100 % 10));
    printf("%d\n", a * (b % 100 / 10));
    printf("%d\n", a * (b / 100));
    printf("%d\n", a * b);
}