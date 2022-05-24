import sys

input = lambda: sys.stdin.readline().rstrip()
pair = lambda : map(int, input().split())

n = 1000 - int(input())
arr = [500,100,50,10,5,1]
res = 0

for i in arr:
    if n >= i:
        res += n // i
        n %= i

print(res)