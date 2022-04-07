import sys

input = sys.stdin.readline
pair = lambda : input().split()

s = input().rstrip()
checkList = [0] * 3

for letter in s:
    if letter == 'A':
        checkList[0] = 1
    elif letter == 'B':
        checkList[1] = 1
    elif letter == 'C':
        checkList[2] = 1

if checkList[0]:
    [print(letter, end = '') if letter not in ['B', 'C', 'D', 'F'] else print('A', end = '') for letter in s] 
elif checkList[1]:
    [print(letter, end = '') if letter not in ['C', 'D', 'F'] else print('B', end = '') for letter in s] 
elif checkList[2]:
    [print(letter, end = '') if letter not in ['D', 'F'] else print('C', end = '') for letter in s]
else:
    print('A' * len(s))