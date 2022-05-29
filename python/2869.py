import sys
import math

input = lambda: sys.stdin.readline().rstrip()
pair = lambda : map(int, input().split())

a, b, v = pair()

res = math.ceil((v-a) / (a-b)) + 1
print(res)