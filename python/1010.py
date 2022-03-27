import sys

input = sys.stdin.readline
pair = lambda : map(int, input().split())

dp = [[0] * 31 for _ in range(31)]

for i in range(30): #행, n
    for j in range(30): #열, r
        if i-j == 0:
            dp[i][j] = 1
        elif j == 1:
            dp[i][j] = i
        elif i >= j:
            dp[i][j] = dp[i-1][j] + dp[i-1][j-1]

for _ in range(int(input())):
    m, n = pair()
    print(dp[n][m])