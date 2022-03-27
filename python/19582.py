import sys
input = sys.stdin.readline
pair = lambda : map(int, input().split())

n = int(input())
arr = sorted([list(pair()) for _ in range(n)], key = lambda x:x[1])
contest = []
depth = 0
money = 0

for i in arr:
    if money <= i[0]:
        contest.append(i)
    else:
    