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

const char* check_VPS(char *str) //���ڿ� ��ȯ�ϱ� ���� �Լ�. https://ggodong.tistory.com/157
{
    int check = 1;
    for (int i = 0; str[i]; i++) {
        if (str[i] == '(') push(str[i]); //�����ٸ� push
        else { //�ݾҴٸ�
            if (empty()) { //����ִٸ� ���� ���� ���� ��. ���� 
                check = 0;
                break;
            }
            else pop(); //push�� ���� ��ȣ ¦��� ����
        }
    }
    if (!empty()) check = 0; //�������� push�ϴ� ��� ���
    while (!empty()) pop(); //���� �ʱ�ȭ. �ϳ��� ���� ���̱⿡.. ���ִ� �͵� �ϳ���. ���Լ��� ����
    
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
    return cnt == 0; //�̷� ���� ��ȯ�� �����ϴ�...
}