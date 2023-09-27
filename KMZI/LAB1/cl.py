import socket
from threading import Thread
from random import randint

from encrypting import generate_rsa_keys, rc4

def send_message(key):
    while True:
        message = input()
        if '!exit' in message:
            client.send(message.encode())
            return
        client.send(rc4(message, key).encode())

def receive_message(key): 
    while True:
        message = client.recv(512).decode()
        print(rc4(message, key))

if __name__ == '__main__':
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 8080))

    message = client.recv(512).decode()
    if "!ready" in message:
        eA, dA, NA = generate_rsa_keys()
        client.send(f"{eA} {NA}".encode())
        eB, NB = map(int, client.recv(512).decode().split()) # получение открытого ключа от другого пользователя

        keyA = randint(100000, 1000000)
        client.send(f"{pow(keyA, eB, NB)}".encode())
        t = client.recv(512).decode()
        keyB = pow(int(t), dA, NA)

        print(f"Обмен ключами произошел. {keyA=}, {keyB=}")

        send_message_thr = Thread(target=send_message, args=(keyB,))
        recv_message_thr = Thread(target=receive_message, args=(keyA,))

        send_message_thr.start()
        recv_message_thr.start()

        send_message_thr.join()
        
        client.close()