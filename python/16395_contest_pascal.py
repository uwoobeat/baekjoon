#16395

import sys

def fact(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

n, k = map(int, sys.stdin.readline().split())
print(int(fact(n-1) / (fact(k-1) * fact(n-k))))