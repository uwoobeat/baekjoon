import sys
sys.setrecursionlimit(10**9)

input = lambda: sys.stdin.readline().rstrip()
pair = lambda : map(int, input().split())

n = int(input())
dp = [-1] * 1000001


def solve(n):
    if n == 1:
        return 0
    if dp[n] != -1:
        return dp[n]
    
    res = solve(n - 1) + 1
    if not n % 3:
        res = min(res, solve(n / 3) + 1)
    if not n % 2:
        res = min(res, solve(n / 2) + 1)
    dp[n] = res
    return dp[n] 

print(solve(n))