"""
a의 최댓값과 b의 최솟값 곱하
"""

import sys
input = sys.stdin.readline

n  = int(input())
a, b = [list(map(int, input().split())) for _ in range(2)]
res = 0

a.sort()

for i in range(n):
    res += a[i] * b.pop(b.index(max(b)))
    
print(res)