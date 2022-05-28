import sys

input = lambda: sys.stdin.readline().rstrip()
pair = lambda : map(int, input().split())

arr = [[i for i in range(1, 15)]] + [[0] * 14 for _ in range(14)]

for i in range(1, 15):
    for j in range(14):
        arr[i][j] = sum(arr[i-1][:j+1])

t = int(input())

for _ in range(t):
    k, n = [int(input()) for _ in range(2)]
    print(arr[k][n-1])