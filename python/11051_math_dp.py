import sys
input = sys.stdin.readline

n, k = map(int, input().split())

def solve(n, k):
    if k == 0 or n == k:
        return 1
    return solve(n-1, k-1) % 10007 + solve(n-1, k) % 100007

print(solve(n, k) % 10007)