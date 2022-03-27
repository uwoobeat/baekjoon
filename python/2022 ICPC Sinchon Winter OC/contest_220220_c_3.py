import sys
from collections import deque
input = sys.stdin.readline
pair = lambda : map(int, input().split())

n = int(input())
a = list(pair())
b = list(pair())
m = int(input())
c = deque(pair())
arr = deque()

for i in range(n):
    if not a[i]:
        arr.appendleft(b[i])
    
for i in range(m):
    if arr:
        print(arr.popleft(), end = ' ')
    else:
        print(c.popleft(), end = ' ')

"""
0의 위치에 있는 요소들 -> 입력한 요소들 순으로 나온다.
"""