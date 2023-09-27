from sys import getsizeof
from bitarray import bitarray


def f(j, x, y, z):
    if j <= 15:
        return x ^ y ^ z
    elif j <= 31:
        return (x & y) | (~x & z)
    elif j <= 47:
        return (x | ~y) ^ z
    elif j <= 63:
        return (x & z) | (y & ~z)
    elif j <= 79:
        return x ^ (y | ~z)


def K1(j):
    if j <= 15:
        return 0x00000000
    elif j <= 31:
        return 0x5A827999
    elif j <= 47:
        return 0x6ED9EBA1
    elif j <= 63:
        return 0x8F1BBCDC
    elif j <= 79:
        return 0xA953FD4E


def K2(j):
    if j <= 15:
        return 0x50A28BE6
    elif j <= 31:
        return 0x5C4DD124
    elif j <= 47:
        return 0x6D703EF3
    elif j <= 63:
        return 0x7A6D76E9
    elif j <= 79:
        return 0x00000000


R1 = [
    0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
    7, 4, 13, 1, 10, 6, 15, 3, 12, 0, 9, 5, 2, 14, 11, 8,
    3, 10, 14,  4,  9, 15,  8,  1,  2,  7,  0,  6, 13, 11,  5, 12,
    1,  9, 11, 10,  0,  8, 12,  4, 13,  3,  7, 15, 14,  5,  6,  2,
    4,  0,  5,  9,  7, 12,  2, 10, 14,  1,  3,  8, 11,  6, 15, 13
]
R2 = [
    5, 14,  7,  0,  9,  2, 11,  4, 13,  6, 15,  8,  1, 10,  3, 12,
    6, 11,  3,  7,  0, 13,  5, 10, 14, 15,  8, 12,  4,  9,  1,  2,
    15,  5,  1,  3,  7, 14,  6,  9, 11,  8, 12,  2, 10,  0,  4, 13,
    8,  6,  4,  1,  3, 11, 15,  0,  5, 12,  2, 13,  9,  7, 10, 14,
    12, 15, 10,  4,  1,  5,  8,  7,  6,  2, 13, 14,  0,  3,  9, 11
]
S1 = [
    11, 14, 15, 12,  5,  8,  7,  9, 11, 13, 14, 15,  6,  7,  9,  8,
    7,  6,  8, 13, 11,  9,  7, 15,  7, 12, 15,  9, 11,  7, 13, 12,
    11, 13,  6,  7, 14,  9, 13, 15, 14,  8, 13,  6,  5, 12,  7,  5,
    11, 12, 14, 15, 14, 15,  9,  8,  9, 14,  5,  6,  8,  6,  5, 12,
    9, 15,  5, 11,  6,  8, 13, 12,  5, 12, 13, 14, 11,  8,  5,  6
]
S2 = [
    8,  9,  9, 11, 13, 15, 15,  5,  7,  7,  8, 11, 14, 14, 12,  6,
    9, 13, 15,  7, 12,  8,  9, 11,  7,  7, 12,  7,  6, 15, 13, 11,
    9,  7, 15, 11,  8,  6,  6, 14, 12, 13,  5, 14, 13, 13,  7,  5,
    15,  5,  8, 11, 14, 14,  6, 14,  6,  9, 12,  9, 12,  5, 15,  8,
    8,  5, 12,  9, 12,  5, 14,  6,  8, 13,  6,  5, 15, 13, 11, 11
]
h0 = 0x67452301
h1 = 0xEFCDAB89
h2 = 0x98BADCFE
h3 = 0x10325476
h4 = 0xC3D2E1F0
h5 = 0x76543210
h6 = 0xFEDCBA98
h7 = 0x89ABCDEF
h8 = 0x01234567
h9 = 0x3C2D1E0F


def ripemd320(message: str):
    bit_array = bitarray()
    bit_array.frombytes(message.encode())
    b = len(bit_array)

    # добавление дополнительных битов
    bit_array.append(1)
    bit_array.extend('0' * ((448 - len(bit_array) % 512) % 512))

    # добавление исходной длины сообщения
    b_bits_lsb = bitarray()
    b_bits_lsb.frombytes(b.to_bytes(4, 'little'))  # 4 байта = 32 бита
    # Преобразование числа b в битовое представление (старшие 32 бита)
    b_bits_msb = bitarray()
    b_bits_msb.frombytes((b >> 32).to_bytes(4, 'little'))  # 4 байта = 32 бита
    # Добавление младших 32 бит числа b к битовой последовательности строки
    bit_array.extend(b_bits_lsb)
    # Добавление старших 32 бит числа b к битовой последовательности строки
    bit_array.extend(b_bits_msb)
    print(len(bit_array), getsizeof(bit_array))
    
    M = [bit_array[i:i+16] for i in range(0, len(bit_array), 16)]

    for i in range(len(M)):
        A1 = h0;   B1 = h1;   C1 = h2;   D1 = h3;   E1 = h4
        A2 = h5;   B2 = h6;   C2 = h7;   D2 = h8;   E2 = h9

        for j in range(79):
            T = (A1 + f(j, B1, C1, D1) + M[i][R1[j]] + K1(j)) << S1[j] + E1
            A1 = E1;   E1 = D1;   D1 = C1 << 10;   C1 = B1;   B1 = T
            T = (A2 + f(79-j, B2, C2, D2) + M[i][R2[j]] + K2(j)) << S2[j] + E2
            A2 = E2;   E2 = D2;   D2 = C2 << 10;   C2 = B2;   B2 = T

            if j == 15:
                B1, B2 = B2, B1
            if j == 31:
                D1, D2 = D2, D1
            if j == 47:
                A1, A2 = A2, A1
            if j == 63:
                C1, C2 = C2, C1
            if j == 79:
                E1, E2 = E2, E1

        A1 += h0;   B1 += h1;   C1 += h2;   D1 += h3;   E1 += h4
        A2 += h5;   B2 += h6;   C2 += h7;   D2 += h8;   E2 += h9

        print(A1)

if __name__ == '__main__':
    print(ripemd320(""))
