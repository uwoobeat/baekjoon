import sys

input = lambda: sys.stdin.readline().rstrip()
pair = lambda : map(int, input().split())

r, c, k = pair()
arr = [list(input()) for _ in range(r)]
visited = [[1 if item == 'T' else 0 for item in line] for line in arr]
dx = [0,0,1,-1]
dy = [1,-1,0,0]
res = 0

print(r, c, k)
print(arr)
print(visited)

def solve(x, y, length):
    global r, c, k, visited, res, dx, dy
    if x == c-1 and y == 0:
        if length == k:
            res += 1
        return
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0 <= nx < c and 0 <= ny < r:
            if visited[ny][nx] != 1:
                visited[ny][nx] = 1
                solve(nx, ny, length+1)
                visited[ny][nx] = 0

visited[r-1][0] = 1
solve(0, r-1, 1)

print(res)