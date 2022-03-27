import sys
input = sys.stdin.readline

t = int(input())
arr = []

for _ in range(t):
    num = int(input())
    if num % 10 == 0 :
        print(1)
    else:
        print(0)
        
    
"""
1,2,1,2 반복
1 -상윤, 2-승우
1이 이기면 0, 2가 이기면 1
4의 경우


"""