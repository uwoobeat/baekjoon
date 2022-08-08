import sys
sys.setrecursionlimit(10**5)

input = lambda: sys.stdin.readline().rstrip()
pair = lambda : map(int, input().split())

n = int(input())
dp = [-1] * (n+2)
dp[0] = 0
dp[1] = 1

def fibo(n):
    if n <= 1:
        return n
    if dp[n] != -1:
        return dp[n]
    dp[n] = fibo(n-1) + fibo(n-2)
    return dp[n]

print(fibo(n))