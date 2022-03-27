#include <stdio.h>
#include <string.h>

int queue[2000001];
int front = 0;
int rear = -1;

void clean(char);
void push(int);
void pop(void);
void size(void);
void empty(void);
int main()
{
    int n, x;
    char str[6];
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%s", str);
        if (!strcmp(str, "push")) {
            scanf("%d", &x);
            push(x);
        }
        else if (!strcmp(str, "pop")) pop();
        else if (!strcmp(str, "size")) size();
        else if (!strcmp(str, "empty")) empty();
        else if (!strcmp(str, "front")) {
            if (rear - front + 1 == 0) printf("%d\n", -1);
            else printf("%d\n", queue[front]);
        }
        else if (!strcmp(str, "back")) {
            if (rear - front + 1 == 0) printf("%d\n", -1);
            else printf("%d\n", queue[rear]);
        }
        memset(str, '\0', sizeof(char));
    }
}

void push(int x)
{
    queue[++rear] = x;
}

void pop(void)
{
    if (rear - front + 1 == 0) printf("%d\n", -1);
    else printf("%d\n", queue[front++]);
}

void size(void)
{
    printf("%d\n", rear - front + 1);
}

void empty(void)
{
    if (rear - front + 1 == 0) printf("%d\n", 1);
    else printf("%d\n", 0);
}