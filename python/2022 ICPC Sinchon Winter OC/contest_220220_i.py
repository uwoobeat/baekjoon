import sys
input = sys.stdin.readline
pair = lambda : map(int, input().split())
n, m = pair()
mod = 1e9 + 7
res = 0

for i in range(1, n+1):
    res += (((n // i) % mod) * ((i % m) % mod)) % mod

print(int(res))