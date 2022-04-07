#WA

import sys

input = lambda: sys.stdin.readline().rstrip()
pair = lambda : map(int, input().split())

def is_palin(s):
    check = 0
    if s == s[::-1]:
        return 0
    for i in range(len(s)):
        if 
    return 2

def is_spalin(s):
    slen = len(s)
    if slen % 2: #짝수이면 4일때 0123중 12 체크, 8이면 0 12 34 56 7이고 34 25 16 07 체크
    

    else: #홀수이면

n = int(input())
for _ in range(n):
    s = input()
    print(is_palin(s))


"""
comcom이면 omcom이 되어야 함
즉 c가 없어지면 omcom
m이 없어지면 comco
첫번째 m이 없어지면 cocom
o가 없어지면 cmcom

즉 comcom의 경우 c와 m이 다르므로 둘 중 하나 없애야 함

"""