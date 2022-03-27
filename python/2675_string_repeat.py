#BOJ 2675 string repeatation

for _ in range(int(input())):
    R, S = input().split()
    string = ""
    for i in S:
        string += i * int(R)
    print(string)