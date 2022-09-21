import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()
pair = lambda : map(int, input().split())

n, m, v = pair()

matrix = [[0] * (n+1) for _ in range(n+1)]
visited = [0] * (n+1)

for _ in range(m):
    x, y = pair()
    matrix[x][y], matrix[y][x] = 1, 1

def dfs(v):
    visited[v] = 1
    print(v, end = ' ')
    for i in range(1, n+1):
        if not visited[i] and matrix[v][i]:
            dfs(i)


def bfs(v):
    dq = deque()
    dq.append(v)
    visited[v] = 1
    while dq:
        v = dq.popleft()
        print(v, end = ' ')
        for i in range(1, n+1):
            if not visited[i] and matrix[v][i]:
                dq.append(i)
                visited[i] = 1

dfs(v)
visited = [0] * (n+1)
print()
bfs(v)