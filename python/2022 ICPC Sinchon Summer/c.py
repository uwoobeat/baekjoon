import sys

input = lambda: sys.stdin.readline().rstrip()
pair = lambda : map(int, input().split())

p, n = pair()
arr = list(pair())
arr.sort(reverse=True)
res = 0

while p < 200:
    p += arr.pop()
    res += 1

print(res)