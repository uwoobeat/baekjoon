#17826 B2 draw_line

"""
선분을 리스트로 설정하는 것이 핵심이었다!

import sys
lst = [0] * 20

for _ in range(int(input())):
    x, y = map(int, sys.stdin.readline().split())
    lst[x:y+1] = [1] * (y-x)
    print(lst)

print(lst.count(1))
"""
import sys
lst = [0] * 10000

for _ in range(int(input())):
    x, y = map(int, sys.stdin.readline().split())
    lst[x-1:y-1] = [1] * (y-x)

print(lst.count(1))