import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()
pair = lambda : map(int, input().split())

m, n = pair()
arr = [list(pair()) for _ in range(n)]
visited = list(arr)
level = [[0] * m for _ in range(n)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
dq = deque()
date = 1
                    
for i in range(n): # y pos
    for j in range(m): # x pos
        if arr[i][j] == 1:
            dq.append((j, i))
            visited[i][j] = 1
            level[i][j] = 1

while dq:
    date += 1
    x, y = dq.popleft() # 노드 빼오기
    date = level[y][x]
    for i in range(4): # 인접 노드 순회
        newx = x + dx[i] # 인접 노드의 좌표
        newy = y + dy[i]
        if 0 <= newx <= m-1 and 0 <= newy <= n-1: # 가능한 범위 내에서
            if arr[newy][newx] == 0 and not visited[newy][newx]: # 안익은 토마토이고 방문하지 않았다면
                dq.append((newx, newy)) # 큐에 추가
                visited[newy][newx] = 1 # 현재 노드 방문처리
                level[newy][newx] = date + 1 # 현재 노드 방문일자 갱신

res = max(map(max, level)) - 1

if 0 in sum(visited, []):
    print(-1)
else:
    print(res)