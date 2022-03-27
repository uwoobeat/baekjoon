import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = sorted([int(input()) for _ in range(n)])
start, end = min(arr), max(arr)+k

"""
3, 10
10 15 20
-> 10 ~ 20+10
-> 평균 20임
-> 10, 15은 20보다 작으므로 count = 10 <= 10
-> res = 10, 시작 +1

"""