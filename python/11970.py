import sys

input = lambda: sys.stdin.readline().rstrip()
pair = lambda : map(int, input().split())

a, b = pair()
c, d = pair()

if b < d:
    a, c = c, a
    b, d = d, b

if a >= d:
    length = b-a+d-c
else:
    length = b-min(a,c)

print(length)