from random import randint

def rand_list(N: int, min:int, max:int) -> list:
    result = []
    for i in range(N):
        result.append(randint(min,max))
    return result

def merge(A:list, B:list) -> list:
    A_i = 0
    B_i = 0
    result = []
    while (A_i<len(A) and B_i<len(B)):
        if A[A_i]<B[B_i]:
            result.append(A[A_i])
            A_i+=1
        else:
            result.append(B[B_i])
            B_i+=1
    result = result+A[A_i:]+B[B_i:]
    return result

def merge_sort(A:list) -> list:
    result = [[A[2*i],A[2*i+1]] for i in range(len(A)//2)]
    for i in range(len(result)):
        if result[i][0]>result[i][1]:
            result[i][0], result[i][1] = result[i][1], result[i][0]
    if len(A)%2 == 1:
        result.append([A[-1]])
    print("sliced:", result)
    while len(result)>1:
        merging_list = []
        for i in range(len(result)//2):
            merging_list.append(merge(result[2*i], result[2*i+1]))
        if len(result)%2 == 1:
            merging_list.append(result[-1])
        result = merging_list
        print(result)
    return result


A = rand_list(11,0,100)
print(A)
print(merge_sort(A))