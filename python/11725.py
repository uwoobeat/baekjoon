import sys
sys.setrecursionlimit(10**6)

input = lambda: sys.stdin.readline().rstrip()
pair = lambda : map(int, input().split())

n = int(input())
matrix = [[] for _ in range(n+1)]
parents = [0] * (n+1)

for _ in range(n-1):
    x, y = pair()
    matrix[x].append(y)
    matrix[y].append(x)


def dfs(v):
    for i in matrix[v]:
        if not parents[i]:
            parents[i] = v
            dfs(i)

dfs(1)

for i in range(2, n+1):
    print(parents[i])