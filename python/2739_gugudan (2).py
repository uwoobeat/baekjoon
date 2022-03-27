'''
BOJ 2739

for multiple   

sol1) assign input() to N
'''
N = int(input())
for i in range(1,10):
    print(f"{N} * {i} = {N*i}")

'''
sol2) No assignmnet for N
'''
for i,j in zip([int(input())]*9,range(1,10)):
    print(f"{i} * {j} = {i*j}")
    
'''
sol3) No assignment for N ver2
'''
for i,j in enumerate([int(input())]*9): #enmurate() return index and value
    print(f"{j} * {i+1} = {(i+1)*j}") 
