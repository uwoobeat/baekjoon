import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
dq = deque()
cnt = 0

for _ in range(n):
    string = input().rstrip()
    if string == "pop":
        try:
            print(dq.popleft())
            cnt -= 1
        except:
            print(-1)
            
    elif string == "size":
        print(cnt)
    elif string == "empty":
        print(1) if not cnt else print(0)
    elif string == "front":
        try:
            print(dq[0])
        except:
            print(-1)
    elif string == "back":
        try:
            print(dq[-1])
        except:
            print(-1)
    else:
        _, x = string.split()
        dq.append(x)
        cnt += 1