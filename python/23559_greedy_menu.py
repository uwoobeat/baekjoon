import sys
input = sys.stdin.readline

n, x = map(int, input().split())
s = [list(map(int, input().split())) for _ in range(n)]

fsum = sum([s[i][1] for i in range(n)])
x -= 1000 * n

diff_flav = list(sorted([s[i][0] - s[i][1] for i in range(n)], reverse = True))

for i in range(n):
    if x >= 4000 and diff_flav[i] >= 0:
        x -= 4000
        fsum += diff_flav[i]

print(fsum)