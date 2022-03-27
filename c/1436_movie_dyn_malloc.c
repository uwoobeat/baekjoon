//1436 re

//666 1666 2666 3666 4666 5666 6660 6666 7666 8666 9666 10666... 15666 16660 16661 ... 16666
/*
c에서는 문자보다 정수로 다루는 것이 더 편리하다. 각 1~3자리에서 666을, 2~4자리에서 666을...
12345를 확인하자.
1000으로 나눈다. 나머지가 666이면 추가한다.
아니라면 10으로 나눈 몫을 보자. 1234다.
1234를 1000으로 나눈다. 나머지(234)가 666인지 확인한다. 몫이 0이라면 탈출한다.
다시 10으로 나눈다. 123이다. 123을 1000으로 나눠 666인지 확인한다. 이것의 몫이 0이라면 탈출한다.
*/

int cond_check(int i)
{
    if (i == 666) return 1;
    else return 0;
}

int quo_zero_check(int i)
{
    if (i / 1000 == 0) return 1;
    else return 0;
}

int main()
{
    int N, num = 666, count = 1;
    scanf("%d", &N);

    while (1)
    {
        while(quo_zero_check(num))
            if (cond_check(num % 1000)) 
            {
                count += 1;
                break;
            }
            else num /= 10;
        
        if (count == N) break;
        num += 1;
    }
    
    printf("%d", num);
}