#BOJ 10952 A+B - 5

while True:
    A, B = map(int, input().split())
    if A == 0 and B == 0:
        break
    else:
        print(A+B)