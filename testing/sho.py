from cryptography.fernet import Fernet
from random import randint
import time
import datetime
import base64
import os
 
def IsPrime(num):
    for n in range(2,int(num**1/2)+1):
        if num%n==0:
            return False
    return True
 
def GenerateGenerator():
    return randint(100, 1000)
 
def GeneratePrime():
    while True:
        numb = randint(100000, 1000000)
        if(IsPrime(numb)):
            prime = numb
            break
    return prime
 
g = GenerateGenerator()
n = GeneratePrime()
 
## Person A
a = randint(10000, 100000)
ga_1 = g ** a
ga = ga_1%n
 
 
## Person B 
b = randint(10000, 100000)
gb_1 = g ** b
gb = gb_1%n
 
 
## Key Calculation
# Person A
key_1 = gb ** a
key = key_1%n
 
 
# Entrypt with Key
with open("E:\\Studing\\testing\\week7_1100.jpg") as file:
    keyraw = '{:032b}'.format(key)
    fernet = Fernet(base64.urlsafe_b64encode(bytes(keyraw,encoding='utf8')))
    encrypted = fernet.encrypt(b"original")
    print(encrypted)
 
 
 
# Person B
key_1 = ga ** b
key = key_1%n
 
 
# Decrypt with Key
keyraw = '{:032b}'.format(key)
fernet = Fernet(base64.urlsafe_b64encode(bytes(keyraw,encoding='utf8')))
decrypted = fernet.decrypt(encrypted)
with open("ret.jpg", 'wb') as file:
    file.write(decrypted)