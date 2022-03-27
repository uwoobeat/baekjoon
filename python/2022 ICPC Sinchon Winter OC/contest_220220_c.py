import time
import sys
from collections import deque
input = sys.stdin.readline
pair = lambda : map(int, input().split())

n = int(input())
a = list(pair())
b = [deque([i]) for i in list(pair())]
m = int(input())
c = list(pair())

start = time.time()

for i in range(m):
    tmp = c[i]
    for j in range(n):
        b[j].appendleft(tmp)
        tmp = b[j].popleft() if a[j] else b[j].pop()
    print(tmp, end = ' ')

end = time.time()

print(end - start)
"""
길이 4
큐는 선입후출 (0)
스택은 선입선출 (1)
2 4 7 입력
큐21팝 스42팝 큐73팝 스4
큐1 스2 큐7 4
2,1 2 3 4
1번 큐이므로 1 pop
2 1,2 3 4
2번 스택이므로 1 pop
2 2 1,3 4
3번 큐이므로 3 pop
2 2 1 3,4
4번 스택이므로 4 pop


"""