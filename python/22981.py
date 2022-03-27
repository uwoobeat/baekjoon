import sys
import math
input = sys.stdin.readline
pair = lambda : map(int, input().split())

n, k = pair()
arr1 = list(sorted(pair()))
arr2 = []
speed = []

for i in range(1, n):
    arr2.append(arr1.pop(0))
    speed.append(arr1[0] * (n-i) + arr2[0] * i)
    print(arr1, arr2)

print(speed)
print(math.ceil(k / max(speed)))