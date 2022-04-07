import sys

input = lambda: sys.stdin.readline().rstrip()
pair = lambda : map(int, input().split())

n = int(input())
arr = list(pair())
arr.sort()
print(arr[-1]-arr[0])