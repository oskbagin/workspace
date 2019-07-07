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
    struct sockaddr_in sa, cli;
    int res, socketFD, err;

    socketFD = socket(AF_INET, SOCK_STREAM, 0);
    if (socketFD == -1)
    {
        perror("Cannot create a socket");
        exit(EXIT_FAILURE);
    }

    memset(&sa, 0, sizeof(sa));

    sa.sin_family = AF_INET;
    sa.sin_port = htons(PORT);
    sa.sin_addr.s_addr = inet_addr(IP_ADDR);

    err = connect(socketFD, (struct sockaddr*)&sa, sizeof(sa));

    if(err == -1)
    {
        perror("Connection failed");
        close(socketFD);
        exit(EXIT_FAILURE);
    }

    u8 tcp_msg[SIZE_1KB], i = 0;
    /* Socket RW here. */
    while(++i < 20)
    {
        sprintf(tcp_msg, "%d) Hello TCP world!", i);
        write(socketFD, tcp_msg, strlen(tcp_msg));
        memset(tcp_msg, 0, SIZE_1KB);
        sleep(1);
    }

    close(socketFD);
    return EXIT_SUCCESS;
}