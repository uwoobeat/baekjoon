#BOJ 2751 S5 num_sort

import sys

N = int(input())
lst = sorted([int(sys.stdin.readline()) for _ in range(N)])

for i in lst:
    print(i)