#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

#include "../ob_commons.h"

#define PORT    5000
#define IP_ADDR "192.168.0.38"

int main(void)
{
    struct sockaddr_in sa = {0};
    int res, err, socketFD;

    socketFD = socket(PF_INET, SOCK_STREAM, IPPROTO_TCP);
    if (socketFD == -1)
    {
        perror("Cannot create a socket");
        exit(EXIT_FAILURE);
    }

    sa.sin_family = AF_INET;
    sa.sin_port = htons(PORT);
    res = inet_pton(AF_INET, IP_ADDR, &sa.sin_addr);

    err = connect(socketFD, (struct sockaddr*)&sa, sizeof(sa) == -1);

    if(err == -1)
    {
        perror("Connection failed");
        close(socketFD);
        exit(EXIT_FAILURE);
    }

    /* Socket RW here. */
    u8 tcp_msg[] = "Hello TCP world!";
    write(err, tcp_msg, strlen(tcp_msg));

    shutdown(socketFD, SHUT_RDWR);

    close(socketFD);
    return EXIT_SUCCESS;
}