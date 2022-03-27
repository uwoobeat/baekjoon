N = int(input())

x1List, y1List, z1List, x2List, y2List, z2List = [[] for _ in range(6)]

for _ in range(N):
    x1, y1, z1, x2, y2, z2 = map(int, input().split())
    x1List.append(x1)
    y1List.append(y1)
    z1List.append(z1)
    x2List.append(x2)
    y2List.append(y2)
    z2List.append(z2)
    
diffList  = [min(x2List) - max(x1List), min(y2List) - max(y1List), min(z2List) - max(z1List)]
x3, y3, z3 = [i if i >= 0 else 0 for i in diffList]
volume = x3 * y3 * z3

print(volume)