from random import randint

def rand_list(N: int, min:int, max:int) -> list:
    result = []
    for i in range(N):
        result.append(randint(min,max))
    return result

def bubble_sort(A: list) -> list:
    for i in range(len(A)):
        flag = 0
        for j in range(0, len(A)-i-1):
            if A[j]>A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
                flag = 1
        if flag == 0:
            break
    return A

A = rand_list(10,0,100)
print(A)
print(bubble_sort(A))