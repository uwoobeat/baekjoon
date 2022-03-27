import time

import sys
from collections import deque
input = sys.stdin.readline
pair = lambda : map(int, input().split())

n = int(input())
a = deque(pair())
b = deque(pair())
m = int(input())
c = deque(pair())

newb = deque()

start = time.time()

while c:
    newb = deque()
    tmp = c.popleft()
    cnt = 0
    while b:
        if a[cnt]:
            newb.append(b.popleft())
        else:
            newb.append(tmp)
            tmp = b.popleft()
        cnt += 1
    print(tmp, end = ' ')
    b = newb

end = time.time()

print(end - start)