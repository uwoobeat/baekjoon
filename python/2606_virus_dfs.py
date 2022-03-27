import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
matrix = [[0] * n for _ in range(n)]
visited = [0] * n

for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    matrix[x-1][y-1] = 1
    matrix[y-1][x-1] = 1

def dfs(v):
    visited[v] = 1
    for i in range(n):
        if matrix[v][i] == 1 and visited[i] == 0:
            dfs(i)
      
dfs(0)
print(visited.count(1)-1)