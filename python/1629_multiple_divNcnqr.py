#1629 multiple_divNcnqr

import sys
input = sys.stdin.readline
a,b,c = map(int, input().split())

def solve(k, n):
    if n == 1:
        return k % c
    else:
        tmp = solve(k, n//2)
        if n % 2 == 0:
            return tmp * tmp % c
        else:
            return tmp * tmp * k % c

print(solve(a,b))

