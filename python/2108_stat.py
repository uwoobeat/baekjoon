#BOJ 2108 S4 stat

import sys

N = int(input())
lst = [int(sys.stdin.readline()) for _ in range(N)]
counterDict = {}

for i in lst:
    if i in counterDict:
        counterDict[i] += 1
    else:
        counterDict[i] = 1

print(round(sum(lst)/N))
print(sorted(lst)[int((N-1)/2)])

freqList = []
for i in counterDict:
    if max(counterDict.values()) == counterDict[i]:
        freqList.append(i)

print(sorted(freqList)[1])
print(max(lst) - min(lst))
