import sys
from collections import Counter
import itertools
sys.setrecursionlimit(10**6)

input = lambda: sys.stdin.readline().rstrip()
pair = lambda : map(int, input().split())

n = int(input())
arr = [list(pair()) for _ in range(n)]
resDict = {-1:0, 0:0, 1:0}    

def solve(y,x,n):
    global resDict
    start = arr[y][x]
    for i in range(y, y+n):
        for j in range(x, x+n):
            if arr[i][j] != start:
                for k in range(3):
                    for l in range(3):
                        step = n//3
                        solve(y+k*step,x+l*step,step)
                return
    resDict[start] += 1
    return

solve(0, 0, n)
for i in resDict.values():
    print(i)