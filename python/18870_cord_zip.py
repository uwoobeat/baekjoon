import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
sorted_arr = sorted(list(set(arr)))
sorted_dic = {sorted_arr[i]:i for i in range(len(sorted_arr))}
print(*[sorted_dic[i] for i in arr])