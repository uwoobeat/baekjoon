#BOJ 2438 print star

for i in range(1, int(input()) + 1):
    print("*" * i)
    
[print("*" * x) for x in range(1, int(input()) + 1)] #little bit faster!