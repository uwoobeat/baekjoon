#1018 S5 chess_repaint

N, M = map(int, input().split())

board = [input() for _ in range(N)]

chessBoard_1 = [list("WBWBWBWB") if i % 2 == 0 else list("BWBWBWBW") for i in range(8)]
chessBoard_2 = [list("BWBWBWBW") if i % 2 == 0 else list("WBWBWBWB") for i in range(8)]
countList = []

for i in range(M-8+1): #column
    for j in range(N-8+1): #row
        checkBoard = [board[j+x][i:i+7] for x in range(7)]
        
