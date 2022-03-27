import sys
input = sys.stdin.readline
sv = list()
for i in range(2,19):
    sv.append(int('1'*i))
nn = int(input())
ans = 0
for j in sv:
    ans += nn//j - nn

print(ans)