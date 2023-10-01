import random
import ctypes

# Функция для проверки простоты числа
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Функция для поиска наибольшего общего делителя
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


# Функция для нахождения обратного по модулю (расширенный алгоритм Евклида)
def mod_inverse(e, phi):
    d = 0
    x1, x2 = 0, 1
    y1, y2 = 1, 0
    while phi != 0:
        quotient = e // phi
        e, phi = phi, e % phi
        x1, x2 = x2 - quotient * x1, x1
        y1, y2 = y2 - quotient * y1, y1
    if x2 < 0:
        x2 += phi
    return x2

def generate_rsa_keys():
    while True:
        p = random.randint(1000000, 10000000)
        if is_prime(p):
            break

    while True:
        q = random.randint(1000000, 10000000)
        if is_prime(q) and q != p:
            break

    # Вычисление N и функции Эйлера phi(N)
    N = p * q
    phi_N = (p - 1) * (q - 1)

    # Выбор числа e (обычно простого, но не обязательно)
    e = random.randint(2, phi_N)
    while gcd(e, phi_N) != 1:
        e = random.randint(2, phi_N)

    # Вычисление числа d, обратного e по модулю phi(N)
    d = mod_inverse(e, phi_N)

    # Вывод открытого и закрытого ключей
    return e, d, N

lib = ctypes.WinDLL(r"E:\Studing\KMZI\LAB3\ripemd320.dll")
lib.ripemd320.restype = ctypes.c_char_p
def ripemd320(message: str) -> int:
    return int(lib.ripemd320(message), 16)
