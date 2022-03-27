import sys
input = sys.stdin.readline

n = int(input())
arr = list(sorted([int(input()) for i in range(n)], reverse=True))
res = -1

for i in range(len(arr)-2):
    if arr[i] < arr[i+1] + arr[i+2]:
        res = arr[i] + arr[i+1] + arr[i+2]
        break

print(res)