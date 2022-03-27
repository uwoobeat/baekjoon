import sys
input = sys.stdin.readline

n = int(input())
arr = sorted(map(int, input().split()))
print(sum([sum(arr[:i+1]) for i in range(n)])) 