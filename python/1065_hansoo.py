#BOJ 1065 num_han

numList = list(map(str, range(1, int(input())+1)))
count = 0

for i in numList:
    temp = list(map(int, list(i)))
    if len(i) == 3:
        if temp[2] - temp[1] == temp[1] - temp[0]:
            count += 1
            
    elif len(i) == 4:
        pass
    
    else:
        count += 1
        
print(count)