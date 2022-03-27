'''
BOJ 10250, Hotel Sol2)
'''

'''
이 문제의 핵심은 두 가지이다.
    1) 꼭대기 층일 때 호수를 기존 방식과 다르게 구해야 함을 인지했는가?
    2) 뒷의 두 자리를 출력할 때 몫이 한 자리인 경우 앞에 0을 붙여야 함을 고려했는가?
        2-sol) 아니면 '자릿수' 개념으로 처리하면 앞에 0 조건을 붙이지 않아도 된다.

첫 번째 풀이에서는 두 줄의 input값을 리스트에 저장한 후,
그 리스트에서 h,w,n 을 각각 분리하여 사용했으나 이는 리스트 선언을 남발하므로 비효율적인 풀이이다.

뿐만 아니라 2-sol)과 같이 자릿수 개념으로 호수를 처리하지 못했으므로 더더욱 그렇다.

두 번째 풀이에서는 이를 피드백 후,
for 하나에 입력과 출력 과정을 모두 통합시켜 효율적인 풀이를 작성해보자.

input1과 input2가 있다면, 꼭 input1 - input2 - output1 - output2 이여야 하는 것이 아니라
input1 - output1 - input2 - output2 역시 정답으로 처리하므로 (즉 입출력 순서는 독립적이므로) 이러한 코딩이 가능하다!
'''

t = int(input())

for x in range(t):
    h, w, n = map(int, input().split())
    
    f = h
    b = n // h
    
    if n % h != 0:
        f = n % h
        b = n // h + 1
        
    print(100*f+b)
    
'''
원래는 if n % h == 0일 떄와 else를 따로 작성해줘야 하나,
f와 b를 미리 n % h 일 때로 할당해두면 !=일 때만 써주면 되므로 스크립트를 더 압축시킬 수 있다.
'''