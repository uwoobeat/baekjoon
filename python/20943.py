import sys
input = sys.stdin.readline
pair = lambda : map(int, input().split())

n = int(input())
res = 0
pos = [list(pair()) for _ in range(n)]
incList = [pos[i][1]/pos[i][0] if (pos[i][0] or pos[i][1]) else 0 for i in range(n)]
incDict = {i : incList.count(i) for i in incList}

while 