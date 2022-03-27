import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(range(n, 0, -1))
case = [0] * n

for i in range(1, n+1):
    if k >= n-i:
        case[i-1] = arr.pop(0)
        k -= n-i
    else:
        case[i-1] = arr.pop(-1)

print(*case) 