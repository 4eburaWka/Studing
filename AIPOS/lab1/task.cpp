#include <winsock2.h>
#include <iostream>
using namespace std;

struct in_addr {  
	union {  
		struct{
		unsigned char
			s_b1, 
			s_b2,
			s_b3,
			s_b4;
		} S_un_b;  
		struct{
		unsigned short
			s_w1,
			s_w2;
		} S_un_w;
		unsigned long S_addr;
	} S_un;
};

struct sockaddr{
	short sin_family;
	unsigned short sin_port;
	struct in_addr sin_addr;
	char sin_zero[8];
};

int main(){
    WORD wVersionRequested;
    WSADATA wsaData;
    int err;

    sockaddr_in service;

    wVersionRequested = MAKEWORD(2, 2);
    err = WSAStartup(wVersionRequested, &wsaData);

    if (err == 0)
        return;
    
    SOCKET socket(AF_INET, SOCK_STREAM, 0);

    bind(socket, (SOCKADDR *) &service, sizeof(service));
    listen(socket, 2);
    accept

    cout << 0;
}