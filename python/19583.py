import sys
input = sys.stdin.readline

s, e, q = map(lambda x : int(x[0:2] + x[3:5]), input().split())
log = {}
res = 0

while 1:
    try:
        time, name = input().split()
        time = int(time[0:2] + time[3:5])
        if name not in log:
            log[name] = [time]
        else:
            log[name].append(time)
    except:
        break

for name in log:
    startCheck = 0
    endCheck = 0
    if len(log[name]) >= 2:
        if log[name].pop(0) <= s:
            startCheck = 1    
        for personLog in log[name]:
            if e <= personLog <= q:
                endCheck = 1
                break
        if startCheck and endCheck:
            res += 1

print(res)