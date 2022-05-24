import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()
pair = lambda : map(int, input().split())

for _ in range(int(input())):
    string = input()
    dq = deque()
    check = 0
    for letter in string:
        if letter == "(":
            dq.append(letter)
        else:
            if dq:
                dq.pop()
            else:
                check = 1
                break
    if dq or check:
        print("NO")
    else:
        print("YES")