import sys

input = lambda: sys.stdin.readline().rstrip()
pair = lambda : map(int, input().split())

def check(a, b, c):
    if a % b == b % c == c % a:
        return True
    else:
        return False

n = int(input())
for _ in range(n):
    a, b, c = pair()
    res = 0
    for i in range(1, a+1):
        for j in range(1, b+1):
            for k in range(1, c+1):
                if check(i, j, k):
                    res += 1
    print(res)