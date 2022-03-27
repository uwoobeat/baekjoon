import sys
input = sys.stdin.readline

n = int(input())

if n == 1:
    print(1)
    exit()

x, y = 1, 0

for i in range(n-2):
    tmp = x
    x += y
    y = tmp

print(x+y)


"""
in operator 이용
숫자에는 1,0 외 다른 숫자 있으면 안됨
만약 1,0 외 숫자로만 구성된 수가 아니라면?
근데 이중 for문이고 길이 기니까 시간초과뜰듯

dp로 풀어야 함 -> 규칙성 찾아야 할듯?
점화식 필요

이친수는 무조건 10으로 시작한다
10을 뺀 나머지 규칙을 찾으면

1 0 (n = 2)
1 1
2 1
3 2
5 3
8 5
"""