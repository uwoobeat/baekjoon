#11049 G3 matrix_dp

import sys
input = sys.stdin.readline

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
dp = [[0 for _ in range(n)] for _ in range(n)] #nxn matrix

for i in range(1, n):
    for j in range(n-i):
        x = j+i
        dp[j][x] = 2 ** 32
        for k in range(j, x):
            dp[j][x] = min(dp[j][x], dp[j][k] + dp[k+1][x] + matrix[j][0] * matrix[k][1] * matrix[x][1])

print(dp)
print(dp[0][n-1])