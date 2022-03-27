"""

"""

import sys

arr = sys.stdin.readline().split()
visited = []
arrlen = len(arr)
arrSum = []

def visit(arr):
    global visited, arrlen, arrSum
    
    num = 1
    
    if arr == []:
        visited.append(sum(arrSum))
        arrSum.pop()
        arr.append(optemp)
        arr.append(numtemp)
        return 0;
    
    if arrSum != []:
        if arr[0] == "-":
            num *= -1
            arr.remove("-")
            optemp = "-"
        else:
            arr.remove("+")
            optemp = "+"
        
    if arr[0] == "+":
        num *= 10
        numtemp = "+"
        arrSum.append(num)
        arr.remove("+")
        visit(arr)
    elif len(arr) >= 2 and arr[0] == "+" and arr[1] == "-":
        num *= 11
        numtemp = zip("+", "-")
        arrSum.append(num)
        arr.remove("+")
        arr.remove("-")
    elif arr[0] == "-":
        numtemp = "-"
        arrSum.append(num)
        arr.remove("-")
    
visit(arr)
print(visited)