import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()
pair = lambda : map(int, input().split())

n = int(input())
arr = [list(pair()) for _ in range(n)]
shark_size = 2
dx = [0,0,1,-1]
dy = [1,-1,0,0]
cur_x, cur_y = 0, 0
INF = 1e9

for i in range(n):
    for j in range(n):
        if arr[i][j] == 9:
            cur_x, cur_y = i, j
            arr[cur_x][cur_y] = 0

def get_dist():
    dist = [[-1] * n for _ in range(n)]
    dq = deque([(cur_x, cur_y)])
    dist[cur_x][cur_y] = 0 # 현재 상어의 위치
    while dq:
        x, y = dq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if arr[nx][ny] <= shark_size and dist[nx][ny] == -1:
                    dq.append((nx, ny))
                    dist[nx][ny] = dist[x][y] + 1
    return dist

def move(dist):
    x, y = 0, 0
    min_dist = INF
    for i in range(n):
        for j in range(n):
            cur_dist = dist[i][j]
            fish_size = arr[i][j]
            if cur_dist != -1 and 1 <= fish_size < shark_size:
                if cur_dist < min_dist: #최소 거리와 좌표 갱신
                    x, y = i, j
                    min_dist = cur_dist
    if min_dist == INF:
        return None
    else:
        return (x, y, min_dist)

time = 0
ate_cnt = 0

while 1:
    pos_data = move(get_dist())
    if not pos_data:
        print(time)
        break
    else:
        cur_x, cur_y, d = pos_data
        time += d
        arr[cur_x][cur_y] = 0
        ate_cnt += 1
    if ate_cnt >= shark_size:
        shark_size += 1
        ate_cnt = 0