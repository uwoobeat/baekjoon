import sys

input = lambda: sys.stdin.readline().rstrip()
pair = lambda : map(int, input().split())

n = int(input())
arr = [list(pair()) for _ in range(n)]
arr.sort(key = lambda x:(x[-1], x[0]))
[print(i[0], i[1]) for i in arr]