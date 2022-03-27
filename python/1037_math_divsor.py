import sys
input = sys.stdin.readline

_ = int(input())
divList = list(map(int, input().split()))
print(min(divList) * max(divList))

"""
4 2 = 8
2 = 4
2 3 4 8 12 = 24

n은 약수들로 떨어지되, 이 약수는 1과 n이 될 수 없다
따라서

8 = 2 ** 3 (2 = 2 ** 1, 4 = 2 ** 2)
4 = 2 ** 2 (2 = 2 ** 1)
24 = 2 ** 3 * 3 ** 1 (2 = 2 ** 1, 12 = 2 ** 2 * 3 ** 1)

-> 최소 인수분해 한 곱 * 최대 인수분해 한 곱
-> 인수가 하나인 것은?
9의 경우 1 3 9
4의 경우 1 2 4
각각 1,9 1,4 제외되므로 그냥 최소 * 최대 적용해도 된다


"""