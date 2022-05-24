import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()
pair = lambda : map(int, input().split())

t = int(input())

for _ in range(t):
    n, m = pair()
    arr = deque(enumerate(pair()))
    res = 0
    mimp = max(arr, key = lambda x : x[1])
    while 1:
        tmp = arr.popleft()
        if tmp != mimp:
            arr.append(tmp)
        else:
            res += 1
            if tmp[0] == m:
                break
            mimp = max(arr, key = lambda x : x[1])
    print(res)