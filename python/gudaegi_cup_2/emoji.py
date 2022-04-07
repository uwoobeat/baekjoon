a = list(input())
b = list(input())
astr = ""
bstr = ""

def convert(emoji):
    if emoji == "\U0001F3B1":
        res = 8
    elif emoji == "\U0001F947":
        res = 1
    elif emoji == "\U0001F948":
        res = 2
    elif emoji == "\U0001F949":
        res = 3
    elif emoji == "\U0001F3B0":
        res = 777
    elif emoji == "\U0001F3EA":
        res = 24
    elif emoji == "\U0001F4C5" or emoji == "\U0001F4C6":
        res = 17
    elif emoji == "\U0001F4AF":
        res = 100
    elif emoji == "0\uFE0F\u20E3":
        res = 0
    elif emoji == "1\uFE0F\u20E3":
        res = 1
    elif emoji == "2\uFE0F\u20E3":
        res = 2
    elif emoji == "3\uFE0F\u20E3":
        res = 3
    elif emoji == "4\uFE0F\u20E3":
        res = 4
    elif emoji == "5\uFE0F\u20E3":
        res = 5
    elif emoji == "6\uFE0F\u20E3":
        res = 6
    elif emoji == "7\uFE0F\u20E3":
        res = 7
    elif emoji == "8\uFE0F\u20E3":
        res = 8
    elif emoji == "9\uFE0F\u20E3":
        res = 9
    elif emoji == "\U00011F51F":
        res = 10
    return res

for i in range(len(a)):
    astr += str(convert(a[i]))

for i in range(len(b)):
    bstr += str(convert(b[i]))

absum = str(int(astr) + int(bstr))

if "777" in absum:
    absum = absum.replace("777", "\U0001F3B0")
elif 
