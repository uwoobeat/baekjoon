import sys
input = sys.stdin.readline
pair = lambda : map(int, input().split())

n, m = [int(input()) for _ in range(2)]
matrix = [[0] * n for _ in range(n)]
visited = [0] * n

for _ in range(m):
    x, y = pair()
    matrix[x-1][y-1] = 1
    matrix[y-1][x-1] = 1

def dfs(d):
    visited[d] = 1
    for i in range(n):
        if matrix[d][i] == 1:
            if visited[i] == 0:
                dfs(i)

dfs(0)
print(visited.count(1)-1)