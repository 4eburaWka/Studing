from cryptography.fernet import Fernet
from random import randint
import base64

#кодирование в Base64
def intoBase64():
    with open("my_image.png", 'rb') as file:
        file_encode_b64 = base64.b64encode(file.read())
    return file_encode_b64

#шифрование
def encrypt(key_a, file_encode_b64):
    keyraw = '{:032b}'.format(key_a)
    fernet = Fernet(base64.urlsafe_b64encode(bytes(keyraw, encoding='utf8')))
    encrypted = fernet.encrypt(file_encode_b64)
    # print(encrypted) # это мы отправляем челу
    return encrypted

#дешифрование
def decrypt(key_b,encrypted):
    keyraw = '{:032b}'.format(key_b)
    fernet = Fernet(base64.urlsafe_b64encode(bytes(keyraw, encoding='utf8')))
    decrypted = fernet.decrypt(encrypted)
    return decrypted

#декодирование из Base64
def fromBase64(decrypted):
    with open("a.png", 'wb') as file:
        file.write(base64.b64decode(decrypted))



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

file_encode_b64=intoBase64()
encrypted=encrypt(key_a, file_encode_b64)
decrypted=decrypt(key_b,encrypted)
fromBase64(decrypted)
