#1436_movie_director_sol2

"""
위의 1)에 따라 이 문제를 풀었을 때의 풀이이다.
조건을 만족하는 수의 리스트를 만들어놓고, 인덱스를 이용하여 N번째에 해당하는 수를 찾는다.

다만 이 풀이의 문제점은 위에서 언급했듯이 다중 반복문을 사용하여 그 구조가 복잡하다는 것이고 
(이는 0000~9999의 수를 생성하기 위함이다. 물론 range를 사용해도 되긴 했다.)

다른 하나는 효율성의 문제이다. 
문제는 맥시멈이 N = 10000일 때를 상정하므로, doomList 역시 10000개의 요소만을 가지는 것이 맞을 것이다.
하지만 len(doomList)는 45991로 이 풀이는 무려 35991번이나 불필요한 연산을 하게 된 것이다.
심지어 2)의 풀이에 따르면 시행 횟수는 N에 따라 줄어드므로 N이 10000이 아니라면 굳이 10000개까지 구할 필요도 없을 것이다.

거기에 중복 요소를 제거하기 위해서 set까지 이용했으니 메모리를 상당히 많이 쳐먹었을 것...!
...라고 생각했는데 꼴랑 4000kb 차이밖에 안나고 심지어 걸린 시간은 sol 2가 무려 7배 가량 빠르다. ??뭐임??
"""

N = int(input())
doomList = []

for i in range(0,5):
    numList = list(["0", "0", "0", "0", "0", "0", "0"])
    numList[i], numList[i+1], numList[i+2] = "6", "6", "6" #determine the "continous area of six"
    
    index_checkList = list([0, 1, 2, 3, 4, 5, 6]) #then choose the left area by index_checkList
    index_checkList.remove(i)
    index_checkList.remove(i+1)
    index_checkList.remove(i+2)
    
    a = index_checkList[0]
    b = index_checkList[1]
    c = index_checkList[2]
    d = index_checkList[3]
    
    for x in range(10): #generate & assign 0000 to 9999
        for y in range(10):
            for z in range(10):
                for w in range(10):
                    numList[a] = str(x)
                    numList[b] = str(y)
                    numList[c] = str(z)
                    numList[d] = str(w)
                    num = "".join(numList)
                    doomList.append(int(num))

doomList = list(set(doomList)) #delete duplicated items
doomList.sort()
print(doomList[N-1])