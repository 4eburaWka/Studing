def merge(A, B):
    '''Слияние двух массивов с сортировкой'''
    C = []
    while len(A) > 0 and len(B) > 0:
        if A[0] < B[0]:
            C.append(A[0])
            A.pop(0)
        else:
            C.append(B[0])
            B.pop(0)

    if len(A) == 0:
        for j in range(len(B)):
            C.append(B[j])
    else:
        for i in range(len(A)):
            C.append(A[i])
    return C



def sorting(arr):
    length = len(arr)
    arr = [[x] for x in arr]    # Создает массив из массивов для каждого числа :: [[1],[5],[62],[...]]
    while len(arr[0]) != length:
        for x in range(len(arr)//2):
            arr[x] = merge(arr[x],arr[x+1])
            arr.pop(x+1)
    return arr[0]


print(sorting([1, 5, 62, 6, 2, 8, 6, 4, 3, 7, 84, 26]))