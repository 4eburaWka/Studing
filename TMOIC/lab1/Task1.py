def Bulean(set):
    '''Возвращает булеан множества'''
    length = len(set)
    Bul = [[] for x in range(2 ** length)]

    # Заполнение массива строками с двоичными числами
    BIN = [bin(x).replace('0b', '0'*(length-len(bin(x))+2)) for x in range(2 ** length)]

    for i in range(2 ** length):
        for j in range(length):
            if BIN[i][j] == '1':
                Bul[i].append(set[j])

    return Bul

A = [1, 2, 4, 7, 8]

print(Bulean(A))

