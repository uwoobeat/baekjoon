import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()
pair = lambda : map(int, input().split())

n, k = pair()
dq = deque(i for i in range(1, n+1))
cnt = 1
arr = list()

while dq:
    if cnt == k:
        arr.append(dq.popleft())
        cnt = 1
    else:
        dq.append(dq.popleft())
        cnt += 1

print("<", end = '')
[print(arr[i], end = ', ') if i != len(arr)-1 else print(arr[i], end = '') for i in range(len(arr))]
print(">", end = '')
