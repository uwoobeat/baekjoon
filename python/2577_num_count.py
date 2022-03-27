#BOJ 2577 num_count

lst = [int(input()) for _ in range(3)]
num = 1
countList = [0] * 10

for i in lst:
    num *= i

for i in str(num):
    countList[int(i)] += 1

for i in countList:
    print(i)