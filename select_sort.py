from random import randint

def rand_list(N: int, min:int, max:int) -> list:
    result = []
    for i in range(N):
        result.append(randint(min,max))
    return result

def select_sort(A: list) -> list:
    for i, val in enumerate(A):
        min_i = i
        for j in range(i, len(A)):
            if A[j]<A[min_i]:
                min_i = j
        A[i], A[min_i] = A[min_i], A[i]
    return A

A = rand_list(10,0,100)
print(A)
print(select_sort(A))