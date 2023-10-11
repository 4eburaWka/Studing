from ctypes import *

from matplotlib import pyplot as plt

lib = WinDLL(r"KMZI/LAB2/r.dll")
lib.ripemd320.argtypes = (c_char_p,)
lib.ripemd320.restype = c_char_p

def ripemd320(message: str) -> int:
    return int(lib.ripemd320(message), 16)

def xor(original_string, two):
    bytes_representation = original_string.encode('latin-1')

    # Преобразование байтов в битовую последовательность
    bit_sequence = list(map(int, list(''.join(format(byte, '08b') for byte in bytes_representation))))
    for i in range(two):
        bit_sequence[len(bit_sequence) - 1 - i] ^= 1
    bit_sequence = list(map(str, bit_sequence))
        
    # Разбиваем битовую последовательность на байты (по 8 бит в каждом)
    byte_array = [''.join(bit_sequence[i:i+8]) for i in range(0, len(bit_sequence), 8)]
    
    # Преобразуем каждый байт в целое число
    int_array = [int(byte, 2) for byte in byte_array]
    
    # Преобразуем целые числа в байты
    byte_string = bytes(int_array)
    
    # Преобразуем байты обратно в строку с использованием кодировки UTF-8
    result_string = byte_string.decode('latin-1')
    
    return result_string
    
def pad_string_to_length(input_string, desired_length):
    padding_length = max(0, desired_length - len(input_string))
    
    padded_string = '0' * padding_length + input_string
    
    return padded_string

def difference_count(num1, num2):
    xor_result = num1 ^ num2
    different_bytes_count = bin(xor_result).count('1')
    return different_bytes_count


def main():
    original_message = '12345'
    original_hash = ripemd320(c_char_p(original_message.encode()))

    bit_mask = 1

    results = []

    for i in range(len(original_message) * 8):
        message = xor(original_message, bit_mask)
        hash = ripemd320(c_char_p(message.encode()))
        print(hash)
        results.append(difference_count(original_hash, hash))
        bit_mask += 1
        if i == 35:
            pass
    plt.plot(range(40), results)
    plt.show()
    print(results)
    


main()