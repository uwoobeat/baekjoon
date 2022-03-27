import sys

N, Q = map(int, input().split())
costList = []
for i in range(N):
    cost = 0
    P, K, C = map(int, sys.stdin.readline().split())
    for i in range(1, Q // K + 1):
        cost += i * C
    cost += P
    costList.append(cost)

print(costList.index(min(costList)) + 1, min(costList))