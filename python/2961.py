import sys
from itertools import combinations

input = lambda: sys.stdin.readline().rstrip()
pair = lambda : map(int, input().split())

n = int(input())
arr = [list(pair()) for _ in range(n)]
arr.sort()
diff = []

for i in range(1, len(arr)+1):
    for j in combinations(arr, i):
        sour = 1
        bitter = 0
        for k in j:
            sour *= k[0]
            bitter += k[1]
        diff.append(abs(bitter-sour))

print(min(diff))