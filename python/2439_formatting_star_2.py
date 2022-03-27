'''
BOJ 2439

star_formatting
'''
N = int(input())
for i in range(1,N+1):
    print(f"%{N}s" %("*"*i))