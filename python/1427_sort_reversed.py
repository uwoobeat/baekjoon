#BOJ 1427

numString = list(input())
numString.sort()
N = ""
for i in numString:
    N = i + N
print(N)