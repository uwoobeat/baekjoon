import sys

n = int(input())
teamList = sorted(list(map(int, sys.stdin.readline().split())))
abilityList = []

for i in range(n):
    abilityList.append(teamList[i] + teamList[2*n-1-i])

print(min(abilityList))