"""
키와 몸 모두 큰 것이 아니면 비교 불가

55 185
58 183
88 186
60 175
46 155

88 186이 둘 다 큼
46 155가 둘 다 작음

만약 키 순으로 정렬했을 때

46 155 0
55 185 1
58 183 2
60 175 3
88 186 4

88 186 1등부터 시작
185보다 175가 작음 -> 2등
175보다 183이 큼 -> 2등 유지 (공동 2등 2명)
183보다 185가 큼 -> 2등 유지 (공동 2등 3명)
185보다 155이 작음 -> 5등 (1+3+1)

만약 1 2 2 4 4 6 이런 결과가 나오려면?
1등 -> 작음 : 1+1 = 2등 -> 큼 : 2등 유지 (2) -> 작음 : 1+2+1 = 4등 ->  작음 : 4+1 = 5등
"""

import sys
input = sys.stdin.readline

n = int(input())
sizeList = sorted([list(map(int, input().split())) + [n] + [i] for i in range(n)])
current = n
print(sizeList)

for i in range(1, n):
    if sizeList[i][1] > sizeList[i-1][1] and sizeList[i][0] > sizeList[i-1][0]:
        sizeList[i][2] = current - 1
    else:
        sizeList[i][2] = sizeList[i-1][2]
    current -= 1

for size in sorted(sizeList, key = lambda x:x[3]):
    print(size[2], end = ' ')