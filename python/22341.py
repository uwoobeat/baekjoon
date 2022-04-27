import sys

input = lambda: sys.stdin.readline().rstrip()
pair = lambda : map(int, input().split())

n, c = pair()
a = n; b = n

for _ in range(c):
    x, y = pair()
    if x >= a or y >= b:
        continue
    elif x * b >= a * y:
        a = x
    else:
        b = y

print(a * b)