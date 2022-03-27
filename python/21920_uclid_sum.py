#BOJ 21920 S4 uclid_average

"""
진정한 상남자라면 gcd쯤은 직접 정의해서 쓰는 게 맞지 않을까...?
"""

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

N = int(input())
A = list(map(int, input().split()))
X = int(input())
numList = []

for i in A:
    if gcd(i, X) == 1:
        numList.append(i)

print(sum(numList) / len(numList))