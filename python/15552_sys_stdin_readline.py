'''
BOJ 15552

sys.stdin.readline()
'''
import sys

for _ in range(int(input())):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    print(x+y)