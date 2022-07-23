import sys

input = lambda: sys.stdin.readline().rstrip()
pair = lambda : map(int, input().split())

n, c = pair()
arr = [int(input()) for _ in range(n)]
arr.sort()

start = 1
end = arr[-1] - arr[0]
res = 0

while start <= end:
    mid = (start + end) // 2
    installedCount = 1
    left = 0
    for right in range(1, n):
        if arr[right] - arr[left] >= mid:
            installedCount += 1
            left = right
    
    if installedCount < c:
        end = mid - 1
    else:
        start = mid + 1
        res = mid

print(res)