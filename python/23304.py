import sys
input = sys.stdin.readline

def is_palin(string):
    return string == string[::-1]

def is_akaraka(string):
    slen = len(string)
    if slen == 1:
        return True
    if is_palin(string):
        return is_akaraka(string[:slen//2]) and is_akaraka(string[-(slen//2):])

print("AKARAKA") if is_akaraka(input().rstrip()) else print("IPSELENTI")