import sys
input = sys.stdin.readline

n = int(input())
r = list(map(int, input().split()))
c = list(map(int, input().split()))

res = r[0] * c[0]
m = c[0]
dist = 0

for i in range(1, n-1):
    if c[i] < m:
        res += m * dist
        dist = r[i]
        m = c[i]
    else:
        dist += r[i]
    
    if i == n-2:
        res += m * dist

print(res)