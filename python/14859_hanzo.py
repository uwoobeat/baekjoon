import sys
N = int(input())
arr = list(map(int, sys.stdin.readline().split()))
killList = []

for i in range(N-1):
    kill = 0
    for j in range(i+1, N):
        if arr[i] > arr[j]:
            kill += 1
        else:
            break
    killList.append(kill)

print(max(killList))