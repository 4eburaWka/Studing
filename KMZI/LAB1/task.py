import socket
from threading import Thread


clients = []

def resend_messages(client: socket.socket):
    while True:
        try:
            data = client.recv(512)
        except ConnectionResetError:
            server.close()
            return
        else:
            if "!exit" in data.decode():
                server.close()
                return
            for cl in clients:
                if cl != client:
                    cl.send(data) 


if __name__ == '__main__':
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 8080))
    server.listen(2)

    while len(clients) != 2:
        client = server.accept()[0]
        print("user connected")
        clients.append(client)
        Thread(target=resend_messages, args=(client,)).start()
    
    clients[0].send("!ready".encode()) 
    clients[1].send("!ready".encode()) 
