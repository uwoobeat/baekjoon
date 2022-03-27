#2908 sangsu

A, B = map(reversed, input().split())

print(max(int(''.join(A)), int(''.join(B))))

#'reversed object' is iterator, so join function on list is needed, not str().
# For instance, 'str(reversed(A))' simply returns the string representation of 'reversed object of A'

#solve 2 - use index operation

A, B = input().split()
A = int(A[::-1])
B = int(B[::-1])

print(max(A, B))