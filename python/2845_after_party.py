#BOJ 2845 - after party

L, P = map(int, input().split())

for i in map(int, input().split()):
    print(i - L * P, end = ' ')