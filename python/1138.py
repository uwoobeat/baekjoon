import sys

input = lambda: sys.stdin.readline().rstrip()
pair = lambda : map(int, input().split())

n = int(input())
arr = list(pair())
line = [0] * n

for i in range(n):
    leftRemain = arr[i]
    for j in range(n):
        if (not leftRemain) and (not line[j]):
            line[j] = i+1
            break
        elif not line[j]:
            leftRemain -= 1

print(*line)