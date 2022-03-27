'''

'''

N = int(input())
for i in range(1,N+1):
    print(f"%{N}s" %("*"*i))

N = int(input())
for i in range(1,N+1):
    print(" "*(N-i),"*"*i)