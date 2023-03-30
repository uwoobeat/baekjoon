from collections import deque

dx = [1,-1,0,0]
dy = [0,0,1,-1]
    

def solution(maps):
    m = len(maps)
    n = len(maps[0])
    
    visited = [[0] * n for _ in range(m)]
    dq = deque()
    visited[0][0] = 1
    dq.appendleft((0,0)) # x, y
    
    while dq:
        x, y = dq.pop()
        
        for i in range(4):
            newx = x + dx[i]
            newy = y + dy[i]
            if 0 <= newx <= 4 and 0 <= newy <= 4:
                if maps[newy][newx] and not visited[newy][newx]:
                    visited[newy][newx] = visited[y][x] + 1
                    dq.appendleft((newx, newy))
    
    answer = visited[m-1][n-1]
    [print(i) for i in visited]
    
    if not answer:
        return -1
    else:
        return answer
    

solution(
    [
    [1, 0, 1, 1, 1], 
    [1, 0, 1, 0, 1], 
    [1, 0, 1, 1, 1], 
    [1, 1, 1, 0, 0], 
    [0, 0, 0, 0, 1]
    ]
)    