import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

n = int(input())
s = input()
dq1 = deque()
dq2 = deque()
res = 0

for i in s:
    if i == 'L':
        dq1.append(i)
    elif i == 'S':
        dq2.append(i)
    elif i == 'R':
        if dq1:
            dq1.pop()
            res += 1
        else:
            break
    elif i == 'K':
        if dq2:
            dq2.pop()
            res += 1
        else:
            break
    else:
        res += 1

print(res)