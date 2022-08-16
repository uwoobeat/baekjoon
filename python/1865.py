import sys

input = lambda: sys.stdin.readline().rstrip()
pair = lambda : map(int, input().split())

INF = 1e9

def solve(start):
    dist[start] = 0
    for i in range(1, n+1):
        for s in range(1, n+1):
            for next, time in arr[s]:
                if dist[next] > dist[s] + time:
                    dist[next] = dist[s] + time
                    if i == n:
                        return True
    return False

tc = int(input())
for i in range(tc):
    n, m, w = pair()
    arr = [[] for _ in range(n+1)]
    dist = [10001 for _ in range(n+1)]
    for j in range(m):
        s, e, t = pair()
        arr[s].append([e, t])
        arr[e].append([s, t])
    for j in range(w):
        s, e, t = pair()
        arr[s].append([e, -t])
    
    x = solve(1)
    if x:
        print("YES")
    else:
        print("NO")