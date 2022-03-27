#BOJ 2475 검증수

"""
1. input().split()으로 고유번호 리스트를 입력받는다.
2. map(int, input().split())으로 리스트의 요소를 정수형으로 변환한다.
3. map()와 lamda x : x**2 를 통해 요소의 제곱 리스트를 만든다.
4. sum()으로 고유번호 제곱의 합을 구한다.
"""
#solve 1
print(sum(map(lambda x : x**2, list(map(int, input().split())))) % 10)

#solve 2
print(sum([int(i) ** 2 for i in input().split()]) % 10)