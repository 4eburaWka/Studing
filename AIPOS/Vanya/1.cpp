#include <iostream>
#include <cstdlib>
#include <cstring>
#include <unistd.h>
#include <arpa/inet.h>
#include <netinet/in.h>
#include <sys/socket.h>

int main() {
    int serverSocket, clientSocket;
    struct sockaddr_in serverAddr, clientAddr;
    socklen_t clientAddrLen = sizeof(clientAddr);

    // Создаем сокет
    serverSocket = socket(AF_INET, SOCK_STREAM, 0);
    if (serverSocket == -1) {
        perror("Ошибка создания сокета");
        exit(EXIT_FAILURE);
    }

    // Настраиваем структуру sockaddr_in для сервера
    memset(&serverAddr, 0, sizeof(serverAddr));
    serverAddr.sin_family = AF_INET;
    serverAddr.sin_addr.s_addr = INADDR_ANY;
    serverAddr.sin_port = htons(12345); // Укажите нужный порт

    // Привязываем сокет к адресу и порту
    if (bind(serverSocket, (struct sockaddr*)&serverAddr, sizeof(serverAddr)) == -1) {
        perror("Ошибка привязки сокета");
        close(serverSocket);
        exit(EXIT_FAILURE);
    }

    // Начинаем слушать входящие соединения
    if (listen(serverSocket, 5) == -1) {
        perror("Ошибка слушания сокета");
        close(serverSocket);
        exit(EXIT_FAILURE);
    }

    std::cout << "Сервер слушает на порту 12345" << std::endl;

    while (true) {
        // Принимаем входящее соединение от клиента
        clientSocket = accept(serverSocket, (struct sockaddr*)&clientAddr, &clientAddrLen);
        if (clientSocket == -1) {
            perror("Ошибка принятия соединения");
            continue;
        }

        // Здесь вы можете добавить обработку клиента и отправлять данные в соответствии с вашими требованиями

        close(clientSocket); // Закрываем соединение с клиентом
    }

    close(serverSocket);
    return 0;
}