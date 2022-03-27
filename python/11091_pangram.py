#11091 pangram

import sys
from string import ascii_lowercase
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    ndict = {alpha : 0 for alpha in ascii_lowercase}
    check = 1
    string = input().lower()
    
    for letter in string:
        if letter.isalpha():
            ndict[letter] = 1
    
    for alpha in ndict:
        if not ndict[alpha]:
            check = 0
            break
    
    if check:
        print("pangram")
    else:
        print("missing", end = ' ')
        for alpha in ndict:
            if not ndict[alpha]:
                print(alpha, end = '')
        print()