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

m, n = pair()

for i in range(m, n+1):
    if is_prime(i):
        print(i)