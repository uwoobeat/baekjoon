'''
BOJ 1110

plus cycle
'''

'''
1. 10보다 작다면, 앞에 0을 붙여 두자리 수로 만들고, 각 자리 숫자를 더한다.
2. 주어진 수의 가장 오른쪽 자리수와 합의 가장 오른쪽 자리수를 이어붙여서 새로운 수를 만든다.
3. 이 때, 이 사이클을 반복하여 원래 수로 돌아오는 반복 횟수를 구한다.
'''

'''
26
8(더하고)
68(합치고)
14(더하고)
84(합치고)
12(더하고)
42(합치고)
6(더하고)
26(합치고)

55
10(더)
50(합)
5(더)
05(합)
5(더)

1 -> 01
1(더)
11(합)
2(더)
12(합)


'''

intInput = input()
start = intInput
count = 0

while True:
    if start == "1":
        count = 60
        break
    
    elif start == "0":
        count = 1
        break
    
    if int(start) < 10:
        
        start = "0" + str(int(start))
    
    digitSum = str(int(start[0]) + int(start[1]))
    newNum = start[-1] + digitSum[-1]
    count += 1
    
    if intInput == newNum:
        break
    
    start = newNum

print(count)