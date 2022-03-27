'''
BOJ 10951

no endpoint -> try - except - else - finally
avoid and generate error
'''
while True:
    try:
        A,B = map(int, input().split())
        print(A+B)
    except:
        break


