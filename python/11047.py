import sys

input = lambda: sys.stdin.readline().rstrip()
pair = lambda : map(int, input().split())

n, k = pair()
arr = [int(input()) for _ in range(n)]
arr.reverse()
res = 0

for i in arr:
    res += k // i
    k %= i

print(res)