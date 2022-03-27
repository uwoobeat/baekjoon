#1436_error_check

N = int(input())
doomList = []

for i in range(0,4):
    for j in range(i+1,5):
        for k in range(j+1,6):
            num_list = list(["0", "0", "0", "0", "0", "0"])
            num_list[i] = "6"
            num_list[j] = "6"
            num_list[k] = "6"
            
            index_checkList = list([0, 1, 2, 3, 4, 5])
            index_checkList.remove(i)
            index_checkList.remove(j)
            index_checkList.remove(k)
            
            a = index_checkList[0]
            b = index_checkList[1]
            c = index_checkList[2]
            
            for x in range(10):
                for y in range(10):
                    for z in range(10):
                        num_list[a] = str(x)
                        num_list[b] = str(y)
                        num_list[c] = str(z)
                        num = "".join(num_list)
                        doomList.append(int(num))

doomList = list(set(doomList))
doomList.sort()
print(doomList)


i = 1
count = 0
check = 1

while count <= 10000:
    if "666" in str(i):
        if check:
            if doomList[count] != i:
                print(count)
                print(doomList[count - 1])
                print(doomList[count])
                print(i)
                check = 0
        count += 1
    if count == N:
        print(i)
        break
    i += 1