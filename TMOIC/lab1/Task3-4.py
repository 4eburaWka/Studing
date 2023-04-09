def bin_mask(A):
    '''Создание битовой маски множества'''
    a_ = [0 for x in range(len(U))]
    for x in range(len(A)):
        if U.index(A[x]) != -1:
            a_[U.index(A[x])] = 1
    return a_

def anti_bin_mask(A):
    C = []
    for x in range(len(A)):
        if A[x] == 1:
            C.append(U[x])
    return C

def union(A, B):
    '''Объединение'''
    c_ = [0 for x in range(len(U))]
    a_ = bin_mask(A)
    b_ = bin_mask(B)
    for x in range(len(a_)):
        c_[x] = a_[x] | b_[x]
    return anti_bin_mask(c_)


def intersection(A, B):
    '''Пересечение'''
    c_ = [0 for x in range(len(U))]
    a_ = bin_mask(A)
    b_ = bin_mask(B)
    for x in range(len(a_)):
        c_[x] = a_[x] & b_[x]
    return anti_bin_mask(c_)


def diff(A, B):
    '''Разность'''
    c_ = [0 for x in range(len(U))]
    a_ = bin_mask(A)
    b_ = bin_mask(B)
    for x in range(len(a_)):
        c_[x] = a_[x] - b_[x]
    return anti_bin_mask(c_)


def sym_diff(A, B):
    '''Симметрическая разность'''
    c_ = [0 for x in range(len(U))]
    a_ = bin_mask(A)
    b_ = bin_mask(B)
    for x in range(len(a_)):
        c_[x] = a_[x] ^ b_[x]
    return anti_bin_mask(c_)
    

def Not(A):
    '''"НЕ"'''
    a_ = bin_mask(A)
    for x in range(len(a_)):
        a_[x] = not a_[x]
    return anti_bin_mask(a_)

U = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
A = [1, 2, 4, 7, 8]
B = [2, 4, 5, 6, 8]
C = [3, 4, 5, 8, 9]

print(intersection(union(A, B), Not(C)))
