#BOJ 1546 average

N = int(input())
lst = list(map(int, input().split()))
M = max(lst)
nlst = [i / M * 100 for i in lst]
print(sum(nlst) / N)