from matplotlib import pyplot as plt
import ctypes

lib = ctypes.WinDLL(r"E:\Studing\KMZI\LAB2\ripemd320.dll")
lib.ripemd320.restype = ctypes.c_char_p


def ripemd320(message: str) -> int:
    # Преобразование хэша в целое число
    hash_hex = lib.ripemd320(message)
    hash_int = int(hash_hex, 16)

    # Первоначальный хэш для сравнения
    original_hash = hash_int

    # Выполняем операции изменения одного бита и сравниваем результаты
    bit_mask = 1
    num_bits = 71  # Длина хэша
    for i in range(num_bits):
        # Инвертируем бит
        modified_hash = hash_int ^ bit_mask

        # Вычисляем новый хэш
        modified_hash_hex = hex(modified_hash)[2:]  # Преобразуем в шестнадцатеричную строку без префикса '0x'
        while len(modified_hash_hex) < len(hash_hex):
            modified_hash_hex = '0' + modified_hash_hex

        # Сравниваем биты измененного и исходного хэша
        num_different_bits = 0
        for j in range(num_bits):
            if hash_hex[j] != modified_hash_hex[j]:
                num_different_bits += 1

        # Выводим информацию о смещении
        print(f"Bit {i + 1}: {num_different_bits} bit(s) difference")

        # Переход к следующему биту
        bit_mask <<= 1

    return original_hash

# Пример использования
message = "Hello, world!"
original_hash = ripemd320(message)
