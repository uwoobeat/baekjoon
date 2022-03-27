T = int(input())
HWN = [input() for _ in range(T)]

regroup = [] 
H = []
W = []
N = []

for x in range(T):
    regroup = HWN[x].split()
    H.append(int(regroup[0]))
    W.append(int(regroup[1]))
    N.append(int(regroup[2]))
    
numRoom = []

for x in range(T):
    if N[x]%H[x] == 0 :
        front = str(H[x])
        back = str(N[x]//H[x])
        if int(back) >= 10:
            numRoom.append(front + back)
        else:
            numRoom.append(front + "0" + back)
    else:
        front = str(N[x] % H[x])
        back = str(N[x] // H[x] + 1)
        if int(back) >= 10:
            numRoom.append(front + back)
        else:
            numRoom.append(front + "0" + back)
    
for i in numRoom:
    print(i)