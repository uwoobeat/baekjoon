import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
dp = arr[:]

for i in range(1, n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j]+arr[i])
        else:
            dp[i] = max(dp[i], arr[i])

print(max(dp))