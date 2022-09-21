import sys
import heapq
sys.setrecursionlimit(10**6)

input = lambda: sys.stdin.readline().rstrip()
pair = lambda : map(int, input().split())

n, m = pair()
k = int(input())
INF = int(1e9)

graph = [[] * (n+1) for _ in range(n+1)]
dist = [INF] * (n+1)

for _ in range(m):
    a, b, c = pair()
    graph[a].append((b, c))

def solve(start):
    q = []
    heapq.heappush(q, (0, start))
    dist[start] = 0
    
    while q:
        d, now = heapq.heappop(q)
        if dist[now] < d:
            continue
        for i in graph[now]:
            cost = d + i[1]
            if cost < dist[i[0]]:
                dist[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

solve(k)

for i in range(1, n+1):
    if dist[i] == INF:
        print("INF")
    else:
        print(dist[i])