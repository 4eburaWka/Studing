from cryptography.fernet import Fernet
from random import randint
import base64


g = randint(1,10)
n = randint(1,10)

# A
a = randint(1,10)
ga = g ** a % n

#B
b = randint(1,10)
gb = g ** b % n

# KEYS
key_a = gb ** a % n
key_b = ga ** b % n


# Кодирование файла в Base64
with open("E:\\Studing\\testing\\week7_1100.jpg", 'rb') as file:
    file_encode_b64 = base64.b64encode(file.read())


# Шифрование
keyraw = '{:032b}'.format(key_a)
fernet = Fernet(base64.urlsafe_b64encode(bytes(keyraw, encoding='utf8')))
encrypted = fernet.encrypt(file_encode_b64)
# print(encrypted) # это мы отправляем челу



# Дешифрование
keyraw = '{:032b}'.format(key_b)
fernet = Fernet(base64.urlsafe_b64encode(bytes(keyraw, encoding='utf8')))
decrypted = fernet.decrypt(encrypted)



with open("E:\\Studing\\testing\\wer.jpg", 'wb') as file:
    file.write(base64.b64decode(decrypted))