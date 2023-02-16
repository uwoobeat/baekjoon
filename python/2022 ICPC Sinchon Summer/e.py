import sys
from collections import deque
sys.setrecursionlimit(10**6)

input = lambda: sys.stdin.readline().rstrip()
pair = lambda : map(int, input().split())

n = int(input())
s = input()
print(s)
tree = [[] for _ in range(n+1)]
visited = [0] * (n+1)
visited[1] = 1
dq = deque()
dq.append(s[0])
res = []

for _ in range(n-1):
    a, b = pair()
    tree[a].append(b)
    tree[b].append(a)

# def dfs(v):
#     for i in tree[v]:
#         if not visited[i]:
#             visited[i] = 1
#             dq.append(i)
#             dfs(i)
#             dq.pop()
#             continue
#     res.append(list(dq))

def solve(v):
    arr = [(i, s[i-1]) for i in tree[v]]
    arr.sort(key=lambda x:x[-1], reverse=True)
    for i in arr:
        idx, weight = i[0], i[1]
        if not visited[idx]:
            visited[idx] = 1
            dq.append(weight)
            solve(idx)
            return dq

print(solve(1))