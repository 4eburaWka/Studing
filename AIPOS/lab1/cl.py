
from datetime import datetime
import socket
import threading

import keyboard
import pyautogui

file = open("log.txt", 'w')

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
while True:
    command = input(">>> ")
    if command.startswith("connect"):
        ip_address, host = command.split()[1:]
        break
client.connect((ip_address, int(host)))
file.write(str(datetime.now()) + " --- connection to server\n")


FLAG = True

def press():
    while True:
        keyboard.wait('home')
        pyautogui.press('Enter')


def input_handler():
    global FLAG
    all_messages = ""
    while FLAG:
        command = input()
        if '~#~' in command:
            client.send(command.encode())
            client.close()
            file.write(str(datetime.now()) + " --- disconnect from server\n")
            break
        all_messages += command
        client.send(command.encode())
        message = client.recv(1024).decode()
        if "!close_connection" in message:
            FLAG = False
            file.write(str(datetime.now()) + " --- disconnect from server\n")
            file.close()
            client.close()
            break
        elif "!control_sum" in message:
            control_sum, last_check = int(message.split()[1]), int(message.split()[2])
            message = client.recv(1024).decode()
            print("Сумма: ", control_sum)
            print("Количество всех символов: ", len(all_messages))
            if control_sum == sum(map(lambda char: ord(char), all_messages[last_check:last_check+48])) and len(all_messages) == int(message.split()[1]):
                print("Сумма верная.")
            else:
                print("Сумма не верная.")
            message = client.recv(1024).decode()
        file.write(message + f" --- {datetime.now()}\n")
        print(message)

# exit_thread = threading.Thread(target=press)
input_thread = threading.Thread(target=input_handler)

# exit_thread.start()
input_thread.start()

# exit_thread.join()
input_thread.join()

client.close()
file.close()