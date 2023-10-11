import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 8080))
server.listen(5)
user_socket, address = server.accept()
print("user connected")

last_check = 0
all_messages = ""
while True:
    data = user_socket.recv(1024)
    all_messages += data.decode()
    if len(all_messages) - last_check > 48:
        control_sum = sum(map(lambda char: ord(char), all_messages[last_check:last_check+48]))
        print("Сумма: ", control_sum)
        print("Количество всех символов: ", len(all_messages))
        user_socket.send(f"!control_sum: {control_sum} {last_check}".encode()) # отправить сумму ASCII 
        user_socket.send(f"!control_len: {len(all_messages)}".encode()) # отправить сумму ASCII 
        last_check += 48
    if '~#~' in all_messages:
        user_socket.send(f"!close_connection".encode())
        user_socket.close()
        break
    print(data.decode())
    user_socket.send(data)