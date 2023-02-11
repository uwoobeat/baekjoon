import sys
import math

input = lambda: sys.stdin.readline().rstrip()
pair = lambda : map(int, input().split())

n = int(input())
if n == 1: print(0)
else: print(math.ceil(n ** 2 / 2))