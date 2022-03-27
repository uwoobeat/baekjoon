import sys
import string from ascii_lowercase
input = sys.stdin.readline
n = int(input())

def is_palin(string):
    return string == string[::-1]

def is_sumi(string):
    return string[:n//2] == string[n//2+1:] if n % 2 else string[:n//2] == string[n//2:]

alphalist = list(ascii_lowercase)
string =  ""

while 1:
    if len(string) < n:
        string += 'a'
        if is_palin(string) and is_sumi(string):
            break
    

print(string)