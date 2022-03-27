#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int stk[100001];
int cnt = 0; //global variable

void push(int n)
{
    stk[cnt] = n;
    cnt++;
}

void pop()
{
    if (cnt != 0) {
        cnt--;
        printf("%d\n", stk[cnt]);
        stk[cnt] = 0;    
    }
    else printf("%d\n", -1);
}

void top()
{
    if (cnt != 0) printf("%d\n", stk[cnt - 1]);
    else printf("%d\n", -1);
}

void size()
{
    printf("%d\n", cnt);
}

void empty()
{
    if (cnt != 0) printf("0\n");
    else printf("1\n");
}

int main()
{
    int n;
    char stack[10];
    scanf("%d", &n);
    int* stk = (int *)malloc(sizeof(int) * n); 
    //dynamic memory allocation instead of "stk[n]" for msvc complier

    for (int i = 0; i < n; i++) {
        scanf("%s", stack);
        if (strcmp(stack, "push") == 0) {
            int num;
            scanf("%d", &num);
            push(num);
        }
        else if (strcmp(stack, "pop") == 0) {
            pop();
        }
        else if (strcmp(stack, "top") == 0) {
            top();
        }
        else if (strcmp(stack, "size") == 0) {
            size();
        }
        else if (strcmp(stack, "empty") == 0) {
            empty();
        }
    }
}