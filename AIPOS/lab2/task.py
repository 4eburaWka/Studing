import socket

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(('localhost', 8080))
print("Сервер запущен и ожидает сообщения...")

all_messages = ""
client_address = None

while True:
    data, client_address = server.recvfrom(1024)
    message = data.decode()
    
    if '~#~' in message:
        server.sendto("!close_connection".encode(), client_address)
        server.close()
        break
    
    all_messages += message
    
    if len(all_messages) > 48:
        control_sum = sum(map(lambda char: ord(char), all_messages[:-48]))
        control_len = len(all_messages)
        
        response = f"!control_sum: {control_sum}"
        server.sendto(response.encode(), client_address)
        response = f" !control_len: {control_len}"
        server.sendto(response.encode(), client_address)
    
    print(message)
    server.sendto(data, client_address)
