'''
BOJ 1712, Calc
'''

'''
<풀이 과정 설계>

고정 비용 A
노트북 당 드는 비용인 가용 비용 B
노트북 가격 C
판매 비용 >= 고정 비용 + 가변 비용인 지점 -> 손익 분기점
C*x >= A + B*x
(C-B)*x = A
x = A/(C-B)
'''

A, B, C = map(int, input().split())

if C-B > 0:
    print(A/(C-B)+1)

else:
    print(-1)

'''
수학에서처럼 변수끼리 나눌 때에는 아래와 같이 항상 변수에 대해 케이스 분류를 해줘야 한다.
    1) C-B>0인 경우
    2) C-B=0인 경우
    3) C-B<0인 경우
    
2), 3)의 경우 x의 해가 존재하지 않으므로 -1을 출력한다. 1)의 경우 정상적으로 x를 출력한다.
'''