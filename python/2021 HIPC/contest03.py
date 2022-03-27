import sys

n, k = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
i = k
cnt = 0
eat = 0

while True:
    if i == len(arr):
        break
    
    if arr[i] > arr[i-k]:
        eat += arr[i] - arr[i-k]
        arr[i] = arr[i-k]
        cnt += 1
        arr.sort()
    else:
        i += 1

print(eat, cnt)