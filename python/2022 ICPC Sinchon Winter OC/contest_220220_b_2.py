import sys
input = sys.stdin.readline
pair = lambda : map(int, input().split())

n = int(input())
arr = [list(pair()) for _ in range(n)]

arr = sorted(arr, key = lambda x : (x[1], x[2], x[3], x[4]))
print(arr)