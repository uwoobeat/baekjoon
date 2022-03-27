'''
BOJ 1731, inference
'''


N = int(input())

num = [int(input()) for _ in range(N)]

decision = 0

for x in range(N-2):
    if num[x+1] - num[x] == num[x+2] - num[x+1]:
        decision = decision + 1

if decision == N-2:
    print(num[N-1] + (num[1]-num[0]))

else:
    print(int(num[N-1] * (num[1]/num[0])))
    
'''
1.
input값이 여러 줄 있다면 for문을 이용하여 input 함수를 여러 번 반복하게 만들면 된다.
예전에 학회 스터디 채널에서 input().split('\n'), 즉 줄바꿈 기호를 기준으로 한번에 입력받으면 안되냐는 질문이 있었는데,
input()값은 무조건 한 줄만을 입력받으므로 이는 불가능하다. (학회 채널 참고)

2.
정수 등비수열 중에서 1~3항까지는 등차수열의 성질을 만족하는 케이스는 없는 것으로 안다.
하지만 스크립트에서는 어느 정도의 엄밀함을 챙겨야 하므로 모든 항에 대해서 등차수열의 성질을 만족하는 지 체크해야 한다.

모든 항에 대해서 if문의 값이 참으로 반환되었을 때~ 를 어떻게 적어야 할 지 몰라서 판정값 개념을 도입했다.
참(1)이면 판정값에 1을 더해나가는 식이다.

우리는 모든 항에 대해서 판정이 참인(등차수열의 성질을 만족하는) 수열을 원하므로,
등차수열의 경우 N-2회의 반복이 끝난다면 판정값은 N-2일 것이다.

만약 아니라면, 제시된 수열은 항상 등차 혹은 등비이므로 등비수열이 된다.

3.
정수 간 나눗셈은 float 자료형으로 출력된다. int()처리를 잊지 말자.
'''
