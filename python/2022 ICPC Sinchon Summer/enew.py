import sys
from collections import deque
sys.setrecursionlimit(10**6)

input = lambda: sys.stdin.readline().rstrip()
pair = lambda : map(int, input().split())

n = int(input())
s = input()
tree = [[] for _ in range(n+1)]
visited = [0] * (n+1)
visited[1] = 1
dq = deque()
dq.append(1)
cand = []
res = []
max_depth = 1

for _ in range(n-1):
    a, b = pair()
    tree[a].append(b)
    tree[b].append(a)

for i in tree:
    i.sort()

def dfs(v, depth, max_depth):
    for i in tree[v]:
        if not visited[i]:
            visited[i] = 1
            dq.append(i)
            dfs(i, depth+1, max_depth)
            max_depth = depth + 1
            dq.pop()
    if depth >= max_depth:
        cand.append(list(dq))

dfs(1,1, max_depth)

for i in cand:
    tmp = ""
    for idx in i:
        tmp += s[idx-1]
    res.append(tmp)

res.sort()
print(res[-1])