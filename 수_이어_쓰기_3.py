import sys

input = lambda: sys.stdin.readline().rstrip()
pair = lambda : map(int, input().split())

n = int(input())
s = ""

for i in range(1, n+1):
    s += str(i)

print(s.find(str(n)) + 1)