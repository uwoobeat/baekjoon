import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()
pair = lambda : map(int, input().split())

n = int(input())
arr = list(pair())
dq = deque()

for i in range(1,n+1):
    skill = arr[n-i]
    if skill == 1:
        dq.appendleft(i)
    elif skill == 2:
        if len(dq) >= 1:
            dq.insert(1, i)
        else:
            dq.append(i)
    elif skill == 3:
        dq.append(i)

print(*dq)