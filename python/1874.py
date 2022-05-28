import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()
pair = lambda : map(int, input().split())


n = int(input())
arr = [int(input()) for _ in range(n)]
dq = deque()
cnt = 0
res = ""

for i in arr:
    while 1:
        if cnt > n:
            print("NO")
            exit()
        if dq:
            if dq[-1] == i:
                dq.pop()
                res += "-"
                break
        cnt += 1
        dq.append(cnt)
        res += "+"

[print(i, end = '\n') for i in res] 