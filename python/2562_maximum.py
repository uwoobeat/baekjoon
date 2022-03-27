#BOJ 2562 maximum
 
lst = [int(input()) for _ in range(9)] #list comprehension
print(max(lst))
print(lst.index(max(lst))+1)