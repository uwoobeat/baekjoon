import sys
sys.setrecursionlimit(10**6)

input = lambda: sys.stdin.readline().rstrip()
pair = lambda : map(int, input().split())

n = int(input())
matrix = [list(map(int, list(input()))) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
dxList = [0, 0, 1, -1]
dyList = [1, -1, 0, 0]
res = []

def dfs(y, x):
    global cnt
    visited[y][x] = 1
    cnt += 1

    for i in range(4):
        newx = x + dxList[i]
        newy = y + dyList[i]
        if 0 <= newx <= n-1 and 0 <= newy <= n-1:
            if not visited[newy][newx] and matrix[newy][newx]:
                dfs(newy, newx)

for y in range(n):
    for x in range(n):
        if not visited[y][x] and matrix[y][x]:
            cnt = 0
            dfs(y, x)
            res.append(cnt)

print(len(res))
[print(i) for i in sorted(res)]