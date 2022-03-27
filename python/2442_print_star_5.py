#BOJ 2442 print_star_5

N = int(input())

for i in range(N):
    print("%s%s" %(" " * (N-i-1), "*" * (2*i + 1)))