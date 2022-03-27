'''
BOJ 11022

A + B - 8
'''
count = int(input())
for i in range(1, count+1):
    A, B = map(int, input().split())
    print(f"Case #{i}: {A} + {B} = {A+B}")