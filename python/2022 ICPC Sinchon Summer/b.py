import sys

input = lambda: sys.stdin.readline().rstrip()
pair = lambda : map(int, input().split())

n = int(input())
arr = list(pair())
prev = 2
bat = 2

for i in range(1, n):
    if arr[i-1] == arr[i]:
        bat += prev * 2
        prev = prev * 2
    else:
        bat += 2
        prev = 2
    if bat >= 100:
        arr[i] = -1
        bat = 0
        prev = 0
        continue

print(bat)