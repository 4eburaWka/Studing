from bitarray import bitarray

# Ваша строка
text = "Hello, Bitarray!"

# Преобразование строки в битовое представление
bit_array = bitarray()
bit_array.frombytes(text.encode('utf-8'))

# Вывод битового представления
print(bit_array)
