import sys

input = lambda: sys.stdin.readline().rstrip()
pair = lambda : map(int, input().split())

t = int(input())
for _ in range(t):
    n = int(input())
    arr = [int(input()) for _ in range(n)]
    vote_max = max(arr)
    vote_sum = sum(arr)
    if arr.count(vote_max) > 1:
        print("no winner")
    else:
        idx = arr.index(vote_max)
        if vote_max > vote_sum / 2:
            print(f"majority winner {idx+1}")
        else:
            print(f"minority winner {idx+1}")