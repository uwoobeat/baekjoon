import sys

N = int(sys.stdin.readline())

for _ in range(N):
    n, m = map(int, sys.stdin.readline().split())
    while True:
        n //= 2
        m += 1
        if n == 0:
            break
    print(m)