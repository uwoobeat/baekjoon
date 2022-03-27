'''
BOJ 1110

plus_cycle_by_recursive
'''
count = 0
targetNum = 0

def cycle(num1, num2 = 0):
    global count, targetNum

    if count == 0:
        targetNum = num1
        
    for i in num1:
        num2 += int(i)
        
    count += 1
    
    num3 = str(num1)[-1]+str(num2)[-1]
    
    if num3 == targetNum:
        return count
    
    return cycle(num3)

def main():
    x = input()
    if x == "1":
        print("60")
    if x == "0":
        print("1")
    else:
        print(cycle(x))
    
main()
    