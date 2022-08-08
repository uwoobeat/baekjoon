import sys

input = lambda: sys.stdin.readline().rstrip()
pair = lambda : map(int, input().split())

n, m = pair()
arr = list()

def solve(depth):
    if depth == m:
        print(*arr)
        return
    
    for i in range(1, n+1):
        if not arr or arr[-1] <= i:
            arr.append(i)
            solve(depth+1)
            arr.pop()

solve(0)