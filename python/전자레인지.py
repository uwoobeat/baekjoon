import sys

input = lambda: sys.stdin.readline().rstrip()
pair = lambda : map(int, input().split())

n = int(input())
[print(n // 300, (n % 300) // 60, ((n % 300) % 60) // 10) if not n % 10 else print(-1)]