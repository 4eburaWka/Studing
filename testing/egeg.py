#!/usr/bin/python3
"""
Client-side chat
"""
try:
    import socket
    import sys
    import time
    import keyboard
    from threading import Thread
except ModuleNotFoundError:
    from subprocess import call
    modules = ["socket", "keyboard"]
    call("pip install " + ' '.join(modules), shell=True)
finally:
    client_socket = socket.socket()
    server_host = socket.gethostname()
    ip = socket.gethostbyname(server_host)
    server_port = 8080

    server_host = input('Enter ip of server: ').strip()
    name = input('Enter your name: ')

    client_socket.connect((server_host, server_port))

    client_socket.send(name.encode())
    server_name = client_socket.recv(1024)
    server_name = server_name.decode()

    def escape():
        while True:
            if keyboard.is_pressed('Esc'):
                client_socket.close()

    print("You joined")
    print("To escape of this chat press: ESC")

    if "__name__" == "__main__":
        Thread(target=escape).start()
        while True:
            message = (client_socket.recv(1024)).decode()
            print(server_name, ">", message)
            message = input("me > ")
            client_socket.send(message.encode())
