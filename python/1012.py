import sys
sys.setrecursionlimit(10**6)

input = lambda: sys.stdin.readline().rstrip()
pair = lambda : map(int, input().split())

t = int(input())
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(x, y):
    visited[y][x] = 1
    for i in range(4):
        newx = x + dx[i]
        newy = y + dy[i]
        if 0 <= newx <= m-1 and 0 <= newy <= n-1:
            if arr[newy][newx] and not visited[newy][newx]:
                dfs(newx, newy)

for _ in range(t):
    m, n, k = pair()
    arr = [[0] * m for _ in range(n)]
    visited = [[0] * m for _ in range(n)]
    cnt = 0

    for _ in range(k):
        pos = list(pair())
        arr[pos[1]][pos[0]] = 1

    for y in range(n):
        for x in range(m):
            if arr[y][x] and not visited[y][x]:
                dfs(x, y)
                cnt += 1
    
    print(cnt)