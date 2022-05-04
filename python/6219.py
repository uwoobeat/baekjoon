import sys

input = lambda: sys.stdin.readline().rstrip()
pair = lambda : map(int, input().split())

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if not n%i:
            return False
    return True

a, b, d = pair()
cnt = 0

for i in range(a, b+1):
    if str(d) in str(i):
        if is_prime(i):
            cnt += 1

print(cnt)