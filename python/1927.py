import sys
import heapq

input = lambda: sys.stdin.readline().rstrip()
pair = lambda : map(int, input().split())
arr = []

n = int(input())

for _ in range(n):
    x = int(input())
    if x == 0:
        if arr:
            print(heapq.heappop(arr))
        else:
            print(0)
    else:
        heapq.heappush(arr, x)