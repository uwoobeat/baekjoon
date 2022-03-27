import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline
pair = lambda : map(int, input().split())

m, n, k = pair()
matrix = [[0] * m for _ in range(n)]
d = [(0,1),(0,-1),(-1,0),(1,0)]

for _ in range(k):
    x1, y1, x2, y2 = pair()
    for i in range(x1, x2):
        for j in range(y1, y2):
            matrix[i][j] = 1

for i in range(m):
    for j in range(n):
        


            

def dfs(x,y):
    matrix[x][y] = 1
    for dx, dy in d:
        x += dx
        y += dy
        if 0 <= x < m and 0 <= y < n and matrix[x][y] == 0:
            return dfs()
        