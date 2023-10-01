import socket
from threading import Thread

from encrypting import generate_rsa_keys, ripemd320

def send_message(key):
    print("Команды:\n!exit - закрыть соединение\n!send - отправить обычное сообщение\n!S__ - отправить подписанное сообщение")
    while True:
        message = input()
        if '!exit' in message:
            client.send(message.encode())
            return
        elif '!S__' in message:
            client.send(message.encode())
            C = pow(ripemd320(message[5:]), key, NA)
            client.send(f"{C}".encode())
            print(f"{C=}, {ripemd320(message)}")
        else:
            client.send(message.encode())

def receive_message(key): 
    while True:
        message = client.recv(2048).decode()
        if '!exit' in message:
            return
        elif '!S__' in message:
            M = message[5:]
            C = int(client.recv(512))
            print(f"{C=}")
            if pow(C, key, NB) == ripemd320(M) % NB:
                print("<Сообщение подписано> ", end='')
            else:
                print("<Сообщение подписано не этим пользователем>")
        print(message)
        


if __name__ == '__main__':
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 8080))
    print("Соединение с сервером установлено.")

    message = client.recv(512).decode()
    if "!ready" in message:
        eA, dA, NA = generate_rsa_keys()
        client.send(f"{eA} {NA}".encode())
        eB, NB = map(int, client.recv(512).decode().split()) # получение открытого ключа от другого пользователя

        print(f"Обмен ключами произошел. {eA=}, {dA=}, {NA=}, {eB=}, {NB=}")

        send_message_thr = Thread(target=send_message, args=(dA,))
        recv_message_thr = Thread(target=receive_message, args=(eB,))

        send_message_thr.start()
        recv_message_thr.start()

        send_message_thr.join()
        
        client.close()