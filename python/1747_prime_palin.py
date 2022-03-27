#1747 S1 check_prime_palin


def is_prime_2(n):
    arr = [False, False] + [True] * (n-1)
    for i in range(2, n+1):
        if arr[i]:
            for j in range(i*2, n+1, i):
                arr[j] = False
    return arr[n]

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if not n%i:
            return False
    return True

def is_palindrome(n):
    tmp = str(n)
    return tmp == tmp[::-1]

n = int(input())

while 1:
    if is_palindrome(n):
        if is_prime(n):
            print(n)
            exit()
    n += 1
