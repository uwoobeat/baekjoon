#17827

import sys

n, m, v = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
newArr = arr[v-1:]

for _ in range(m):
    k = int(sys.stdin.readline())
    if k <= n - 1:
        print(arr[k])
    else:
        print(newArr[(k-n)%(n-v+1)])