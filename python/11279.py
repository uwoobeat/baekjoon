import sys
import heapq

input = lambda: sys.stdin.readline().rstrip()
pair = lambda : map(int, input().split())

n = int(input())
arr = []

for _ in range(n):
    x = int(input())
    if x:
        heapq.heappush(arr, (-x, x))
    else:
        if len(arr) >= 1:
            print(heapq.heappop(arr)[1])
        else:
            print(0)