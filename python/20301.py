import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()
pair = lambda : map(int, input().split())

n, k, m = pair()
dq = deque(i for i in range(1, n+1))
cnt_dir = 0
cnt_ord = 1
while dq:
    if cnt_dir == m:
        dq = deque(reversed(dq))
        cnt_dir = 0
    if cnt_ord == k:
        print(dq.popleft())
        cnt_ord = 1
        cnt_dir += 1
    else:
        dq.append(dq.popleft())
        cnt_ord += 1
