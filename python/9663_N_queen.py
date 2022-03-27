#9663 G5 N-queen

"""
 3.8ë¡œëŠ” ?‹œê°„ì´ˆê³? ë°œìƒ (???ë¶?ë¶„ì˜ ë°±íŠ¸?ž˜?‚¹ ë¬¸ì œ?Š” ?ŒŒ?´?¬ ê¶Œìž¥ ?•ˆ?•¨)
-> pypy3ë¡? ?‹¤?–‰?•˜?Š” ê²? ê¶Œìž¥
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