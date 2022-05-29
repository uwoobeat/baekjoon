import sys

input = lambda: sys.stdin.readline().rstrip()
pair = lambda : map(int, input().split())

a, b = pair()
check = [1 for _ in range(b-a+1)]
cnt = 0

for i in [i**2 for i in range(2, int(b**0.5)+1)]:
    idx = a//i * i - a
    while idx <= b-a:
        if 0 <= idx <= b-a:
            check[idx] = 0
        idx += i

print(sum(check))