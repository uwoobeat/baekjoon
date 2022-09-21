import sys
sys.setrecursionlimit(10**6)

input = lambda: sys.stdin.readline().rstrip()
pair = lambda : map(int, input().split())

n, m = pair()
matrix = [[0] * (n+1) for _ in range(n+1)]
visited = [0] * (n+1)
cnt = 0

for _ in range(m):
    x, y = pair()
    matrix[x][y], matrix[y][x] = 1, 1

def dfs(v):
    visited[v] = 1
    for i in range(1, n+1):
        if not visited[i] and matrix[v][i]:
            dfs(i)

for i in range(1, n+1):
    if visited[i]:
        continue
    dfs(i)
    cnt += 1

print(cnt)