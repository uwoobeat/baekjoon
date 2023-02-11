import sys

input = lambda: sys.stdin.readline().rstrip()
pair = lambda : map(int, input().split())

n = int(input())
s = input()

lst = [s.count("H"), s.count("I"), s.count("A"), s.count("R"), s.count("C")]
print(min(lst))