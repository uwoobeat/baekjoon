import sys

input = lambda: sys.stdin.readline().rstrip()
pair = lambda : map(int, input().split())

board = [list(pair()) for _ in range(9)]
blankPosList = [(i,j) for i in range(9) for j in range(9) if not board[i][j]]

def check(i, j):
    nums = [1,2,3,4,5,6,7,8,9]
    for k in range(9):
        if board[i][k] in nums:
            nums.remove(board[i][k])
        if board[k][j] in nums:
            nums.remove(board[k][j])
    for y in range(i//3*3, i//3*3+3):
        for x in range(j//3*3, j//3*3+3):
            if board[y][x] in nums:
                nums.remove(board[y][x])
    return nums

def solve(cnt):
    if cnt == len(blankPosList):
        for line in board:
            print(*line)
        exit(0)
    (i, j) = blankPosList[cnt]
    for x in check(i, j):
        board[i][j] = x
        solve(cnt+1)
        board[i][j] = 0

solve(0)