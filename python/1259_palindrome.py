#BOJ 1259 B1 palindrome

"""
문제를 꼼꼼히 보는 습관을 들이는 편이...
"""

while True:
    try:
        N = input()
        if N != "0":
            if N == ''.join(reversed(N)):
                print("yes")
            else:
                print("no")
    except EOFError:
        break