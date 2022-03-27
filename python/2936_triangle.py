#BOJ 2936 B2 vegan_triangle

"""
솔직히 case 1~6으로 나눌 필요 없이 두 조건을 합쳐버리면 코드가 더 간단해진다.
근데 저게 뭔가 이해하기엔 좋아서 그대로 냅뒀다.
키보드에 손부터 가는 습관을 고치자...
"""
x, y = map(int, input().split())

if x == 0:
    if 0 <= y <= 125:
        case = 1
    else:
        case = 2
elif y == 0:
    if 0 < x <= 125:
        case = 6
    else:
        case = 5
else:
    if x <= 125 and y >= 125:
        case = 3
    else:
        case = 4

if case == 1:
    k = 1/2 * 250 * 250 / (250 - y)
    s, t = k, 250 - k
elif case == 2:
    k = 1/2 * 250 * 250 / y
    s, t = k, 0
elif case == 3:
    k = 250 - (1/2 * 250 * 250 / y)
    s, t = k, 0
elif case == 4:
    k = 250 - (1/2 * 250 * 250 / x)
    s, t = 0, k
elif case == 5:
    k = 1/2 * 250 * 250 / x
    s, t = 0, k
elif case == 6:
    k = 250 - (1/2 * 250 * 250 / (250 - x))
    s, t = k, 250 - k

print("%.2f %.2f" %(s, t))