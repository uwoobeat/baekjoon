#include <stdio.h>

char stack[50];
int cnt = 0;

const char* check_VPS(char *);
void push(char);
char pop();
int empty();

int main()
{
    int t;
    char arr[51];
    scanf("%d", &t);
    for (int i = 0; i < t; i++) {
        scanf("%s", arr);
        printf("%s", check_VPS(arr));
    }
}

const char* check_VPS(char *str) //문자열 반환하기 위한 함수. https://ggodong.tistory.com/157
{
    int check = 1;
    for (int i = 0; str[i]; i++) {
        if (str[i] == '(') push(str[i]); //열었다면 push
        else { //닫았다면
            if (empty()) { //비어있다면 열기 전에 닫은 것. 거짓 
                check = 0;
                break;
            }
            else pop(); //push된 여는 기호 짝지어서 없앰
        }
    }
    if (!empty()) check = 0; //마지막에 push하는 경우 고려
    while (!empty()) pop(); //스택 초기화. 하나씩 들어가는 것이기에.. 빼주는 것도 하나씩. 후입선출 구현
    
    if (check) return "YES\n";
    else return "NO\n";
}

void push(char c)
{
    cnt++;
    stack[cnt] = c; //or stack[cnt++]
}

char pop()
{
    cnt--;
    return stack[cnt]; //or stack[--cnt]
}

int empty()
{
    return cnt == 0; //이런 식의 반환도 가능하다...
}