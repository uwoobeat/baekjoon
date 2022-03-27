x, y = [int(input()) for _ in range(2)]

if y > 0:
    if x > 0:
        print("1")
    else:
        print("2")
else:
    if x < 0:
        print("3")
    else:
        print("4")