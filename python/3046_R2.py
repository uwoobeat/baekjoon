#BOJ 3046 R2

"""
S = R1 + R2 / 2
그런데 R1과 S가 주어짐
R2는?
2S - R1 = R2
"""

R1, S = map(int, input().split())
print(2*S - R1)
