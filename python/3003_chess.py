#BOj 3003 chess

for x, y in zip([1, 1, 2, 2, 2, 8], map(int, input().split())):
    print(x-y, end = ' ')