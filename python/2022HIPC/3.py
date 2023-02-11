import sys

input = lambda: sys.stdin.readline().rstrip()
pair = lambda : map(int, input().split())

n, k = pair()
board = [[0] * (n+2) for _ in range(n+2)]

r, c = pair() # 2 means white king
board[r][c] = 2
offset = [[-1,0], [-1,1], [0,1], [1,1], [1,0], [1,-1], [0,-1]] # 맨 위부터 시계방향

for _ in range(k):
    i, j = pair()
    board[i][j] = 1 # 1 means black quuen
    for p in range(1, n+1):
        board[i][p] = 1
        board[p][j] = 1
        board[p][n-p] = 1
        board[p][i+j-p] = 1
        if (p+abs(i-j)) <= n:
            if i >= j:
                board[p+(i-j)][p] = 1
            else:
                board[p][p+(j-i)] = 1

for i in range(n+2): # fill outline
    board[0][i] = 3 # 3 means not available
    board[n+1][i] = 3
    board[i][0] = 3
    board[i][n+1] = 3

flag = False
for y, x in offset:
    if board[r+y][c+x] == 0:
        flag = True

if board[r][c] == 1 and flag:
    print("CHECK")
elif board[r][c] == 1 and not flag:
    print("CHECKMATE")
elif board[r][c] == 2 and not flag:
    print("STALEMATE")
else:
    print("NONE")

# for line in board:
#     print(*line)
"""
5 1
2 2
3 2

for line in board:
    print(*line)
"""