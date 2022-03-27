import sys
input = sys.stdin.readline

k, n = map(int, input().split())
arr = [int(input()) for _ in range(k)]
start = 1
end = max(arr)

while start <= end:
    mid = (start + end) // 2
    cnt = sum([i//mid for i in arr]) #for문보다 sum이 더 빠름
    if cnt >= n:
        start = mid + 1
    else:
        end = mid - 1

print(end)