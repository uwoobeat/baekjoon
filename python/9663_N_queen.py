#9663 G5 N-queen

"""
 3.8λ‘λ ?κ°μ΄κ³? λ°μ (???λΆ?λΆμ λ°±νΈ??Ή λ¬Έμ ? ??΄?¬ κΆμ₯ ??¨)
-> pypy3λ‘? ?€??? κ²? κΆμ₯
"""


import sys

def check(n):
    for i in range(n):
        if board[n] == board[i] or abs(board[n] - board[i]) == n - i:
            return 0
    return 1

def visit(index):
    global result
    
    if index == n:
        result += 1
    else:
        for i in range(n):
            board[index] = i
            if check(index):
                visit(index + 1)

n = int(sys.stdin.readline())
board = [0] * n
result = 0
visit(0)
print(result)