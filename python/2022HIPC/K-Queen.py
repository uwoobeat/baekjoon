import sys

input = lambda: sys.stdin.readline().rstrip()
pair = lambda : map(int, input().split())

n, k = pair()
r, c = pair()

board = []
check = [[0] * 3 for _ in range(3)]
offset = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,0],[0,1],[1,-1],[1,0],[1,1]]

for i in range(9):
    board.append([r+offset[i][0], c+offset[i][1]])


for _ in range(k):
    i, j = pair()
    if r-1 <= i <= r+1:
        diff = i-(r-1)
        check[0][diff] = 1
        check[1][diff] = 1
        check[2][diff] = 1
    if c-1 <= j <= c+1:
        diff = j-(c-1)
        check[diff][0] = 1
        check[diff][1] = 1
        check[diff][2] = 1
    if r+c-2 <= i+j <= r+c+2:
        diff = (i+j) - (r+c-2)
        for i in range(diff+1):
            check[i][diff-i] = 1
    if r-c-2 <= i-j <= r-c+2:
        diff = (i-j) - (r-c-2)
        for i in range(diff+1):
            check[i][] = 1

# for line in check:
#     print(*line)

if sum([sum(line) for line in check]) == 9:
    print("CHECKMATE")
elif sum([sum(line) for line in check]) == 8 and check[2][2] == 0:
    print("STALEMATE")
elif check[2][2] == 1:
    print("CHECK")
else:
    print("NONE")
    
"""
5 1
2 2
3 2

for line in board:
    print(*line)

체크 = 검퀸 y리스트 중에 흰킹 y, ...
체크메이트 = 검퀸 x리스트 중에 
"""