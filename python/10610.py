import sys

input = lambda: sys.stdin.readline().rstrip()

n = sorted(list(input()), reverse=True)
res = 0

for i in n:
    res += int(i)
if res % 3 != 0 or "0" not in n:
    print(-1)
else:
    print(''.join(n))