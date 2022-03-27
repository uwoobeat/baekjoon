h, m = map(int, input().split())

if m >= 45:
    print(h, m-45)

else:
    if h == 0:
        print(23, m+15)
    else:
        print(h-1, m+15)

'''
if h == 0:
    h == 24
    
0 45 -> 24 0
0 45+이면 강제적으로 24가 된다.
'''