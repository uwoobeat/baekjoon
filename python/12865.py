import sys

input = lambda: sys.stdin.readline().rstrip()
pair = lambda : map(int, input().split())

n, k = pair()
arr = [list(pair()) for _ in range(n)]
dp = [[0] * (k+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, k+1):
        w = arr[i-1][0]
        v = arr[i-1][1]
        if j < w:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j-w]+v, dp[i-1][j])

print(dp[n][k])

"""
0-1 knapsack 문제

1. 허용 무게보다 크면 안넣고 이전 가치 그대로
2. 아니라면 현재 무게만큼 뺀 dp의 가치 + 현재 가치와 이전 가치 비교
"""