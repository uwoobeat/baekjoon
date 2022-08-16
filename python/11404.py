import sys

input = lambda: sys.stdin.readline().rstrip()
pair = lambda : map(int, input().split())

n = int(input())
m = int(input())
INF = 10e9

arr = [[INF] * n for i in range(n)]

for i in range(m):
    a, b, c = pair()
    if arr[a-1][b-1] > c:
        arr[a-1][b-1] = c

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i != j and arr[i][j] > arr[i][k] + arr[k][j]:
                arr[i][j] = arr[i][k] + arr[k][j]

for i in arr:
    for j in i:
        if j == INF:
            print(0, end = ' ')
        else:
            print(j, end = ' ')
    print()                