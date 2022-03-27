"""
PyPy3로는 메모리 초과...
상하좌우를 조사하면서 탐색하고, 1회 탐색 끝나면 cnt += 1
"""

import sys
sys.setrecursionlimit(10000000) #파이썬으로 재귀 문제 풀 때는 필수. 최대 재귀 깊이를 늘린다

n = int(sys.stdin.readline())
matrix = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1 ,1]
cnt_1, cnt_2 = 0, 0

def dfs(x, y):
    visited[x][y] = 1
    color = matrix[x][y]
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx < n) and (0 <= ny < n): #out of index 방지
            if visited[nx][ny] == 0:
                if matrix[nx][ny] == color:
                    dfs(nx, ny)

for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            dfs(i, j)
            cnt_1 += 1

for i in range(n):
    for j in range(n):
        if matrix[i][j] == 'R':
            matrix[i][j] = 'G'

visited = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            dfs(i, j)
            cnt_2 += 1

print(cnt_1, cnt_2)