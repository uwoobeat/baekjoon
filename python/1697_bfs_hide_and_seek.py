import sys
from collections import deque

def bfs():
    q = deque()
    q.append(n)
    while q:
        x = q.popleft()
        if x == k:
            print(visited[x])
            break
        
        for i in [x-1, x+1, x*2]:
            if 0 <= i <= 100000 and not visited[i]: #exclude dup item
                visited[i] = visited[x] + 1 #time += 1
                q.append(i)
                

n, k = map(int, sys.stdin.readline().split())
visited = [0] * 100001
bfs()