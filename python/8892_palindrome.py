#8892 S5 palindrome

import sys
input = sys.stdin.readline

t = int(input())

def check(string):
    if string == string[::-1]:
        return True
    else:
        return False

for _ in range(t):
    try:
        k = int(input())
        lst = [input().rstrip() for _ in range(k)]
        for i in range(k):
            for j in range(k):
                if i != j:
                    word = lst[i] + lst[j]
                    if check(list(word)):
                        raise checked
    except:
        print(word)
    else:
        print(0)

"""
for _ in range(t):
    k = int(input())
    lst = [input().rstrip() for _ in range(k)]
    cnt = 0
    for i in range(i):
        for j in range(j):
            if i != j:
                word = lst[i] + lst[j]
                if check(word):
                    raise checked
"""                