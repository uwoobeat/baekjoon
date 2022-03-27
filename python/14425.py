import sys
input = sys.stdin.readline
pair = lambda : map(int, input().split())

n, m = pair()
s = [input().rstrip() for _ in range(n)]
res = 0

for i in range(m):
    if input().rstrip() in s:
        res += 1

print(res)