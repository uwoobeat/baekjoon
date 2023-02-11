import sys

input = lambda: sys.stdin.readline().rstrip()
pair = lambda : map(int, input().split())

t = int(input())
arr = [int(input()) for _ in range(t)]
dp = [[0, 0] for _ in range(41)]
dp[0] = [1,0]
dp[1] = [0,1]
dp[2] = [1,1]

for i in range(3, 41):
    dp[i][0] = dp[i-1][0] + dp[i-2][0]
    dp[i][1] = dp[i-1][1] + dp[i-2][1]

for i in arr:
    print(dp[i][0], dp[i][1])