import sys
import math

T = int(input())
lst = map(int, [sys.stdin.readline() for _ in range(T)])
dList = [0]

for i in range(63):
    dList.append(((-1) ** i) * (2 ** math.floor(i / 2)))

for x in lst:
    time = 0
    i = 0
    while True:
        if not (dList[i] <= x <= dList[i+1] or dList[i+1] <= x <= dList[i+1]):
            time += abs(dList[i] - dList[i+1])
            i += 1
        else:
            time += abs(x - dList[i])
            break
    print(time)