#1018 S5 chess_repaint_2

N, M = map(int, input().split())

board = [input() for _ in range(N)]
numList = []

for i in range(N-8+1):
    for j in range(M-8+1):
        num1 = 0
        num2 = 0
        for x in range(8):
            for y in range(8):
                if (x+y) % 2 == 0:
                    if not board[i+x][j+y] == "W":
                        num1 += 1
                else:
                    if not board[i+x][j+y] == "B":
                        num1 += 1
        for x in range(8):
            for y in range(8):
                if (x+y) % 2 == 0:
                    if not board[i+x][j+y] == "B":
                        num2 += 1
                else:
                    if not board[i+x][j+y] == "W":
                        num2 += 1
        numList.append(min(num1, num2))

print(min(numList))