'''
BOJ 10998, AxB
'''

A,B = map(int, input().split())
print(A*B)

'''
map() 함수는 built-in 함수로 list 나 dictionary 와 같은 iterable(반복가능)한 데이터를 인자로 받아
list 안의 개별 데이터를 함수의 인자로 전달하여 결과를 list 형태로 반환해 주는 함수이다.

즉 위 예제는 input().split()에서 받은 list를(x.split()은 문자열 x를 공백 기준으로 나누어 리스트 자료형으로 반환한다)
int()의 인자로 각각 할당해주는 것이다.
'''