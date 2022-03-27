#BOJ 1193 B2 hate_math_2

"""
세로 열 - y
가로 열 - x
즉, y/x 꼴이다. 가령 3행 2열의 경우 x=3, y=2로 2/3이다.

번호들을 1/2/3...의 묶음으로 쪼갠다.
묶음에서는 분모와 분자의 합이 일정하다! 이 성질을 이용하는 것이 핵심.
대충 몇번째 묶음인지 확인하고, 묶음에서의 위치를 통해 x,y를 구하면 된다.
"""

#solve 1

N = int(input())
count = 2
start = 1
end = 1

while True:
    if not start <= N <= end:
        start = end + 1
        end += count
        count += 1
    else:
        break

if not count % 2:
    x_start = 1
    y_start = count - 1
    distance = N - start
    x = x_start + distance
    y = y_start - distance
else:
    x_start = count - 1
    y_start = 1
    distance = N - start
    x = x_start - distance
    y = y_start + distance

print(f"{y}/{x}")


#solve 2

"""
while문은 최대한 간결해야만 한다. 수학으로 치면 '체계적인 노가다'가 while문이 하는 일이다.
두 경계 사이에 있는지 확인하는 것보다,
경계를 넘는지 확인하고 - 확인한 범위를 지우고 - 다음 범위를 확인하는 것이 더 효율적이다. 배울 점이 많은 코드...!
"""

N = int(input())
count = 1

while N > count:
    N -= count
    count += 1

x = N
y = count + 1 - N
if count % 2 == 1:
    x, y = y, x

print(f"{x}/{y}")

"""
이렇게 되면 묶음 순서에 해당하는 count와 묶음에서 몇 번째인지를 보이는 N이 남는다.
짝수번째 묶음의 경우 (1,sum-1) 부터 시작한다. 따라서 묶음 내 순서가 N이면 (N, 합 - N)이다.
합은 묶음 수 + 1이므로 좌표는 (N, count+1-N)이다. 
"""