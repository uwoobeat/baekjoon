#BOJ 1550 hexadecimal

"""
1. 16진수를 입력받는다.
2. 16진수의 각 자리 수를 읽는다.
3. 각 자리 수에 맞게 16승을 하여 더한다.
4. 더한 값을 10진수로 하여 출력한다.
"""

hexanum = reversed(input())
convertDict= {"A": 10, "B" : 11, "C" : 12, "D" : 13, "E" : 14, "F" : 15}
decinum = 0
count = 0

for letter in hexanum:
    if letter.isalpha():
        letter = convertDict[letter]
    else:
        letter = int(letter)
    decinum += letter * (16 ** count)
    count += 1

print(decinum)

#solve 2 - base parameter of int()

print(int(input(), 16))