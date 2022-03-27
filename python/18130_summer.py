#BOJ 18130 B2 summer_fan_cost

"""
timeout을 어떻게 컨트롤 할 것인지가 핵심인듯?
등차수열의 합을 for이나 range를 돌면서 구하게 되면 무조건 시간초과가 난다.
합 = 등차중항 * 항의 개수의 성질을 이용하면 될 듯한데, 자꾸 에러 발생...
"""

import sys

#solve 1 - bip

N, Q = map(int, input().split())
costList = []
for i in range(N):
    cost = 0
    P, K, C = map(int, sys.stdin.readline().split())
    cost += P + ((1 + Q // K) * C * (Q // K) / 2)
    costList.append(int(cost))

print(costList.index(min(costList)) + 1, min(costList))

#sovle 2 - timeout

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