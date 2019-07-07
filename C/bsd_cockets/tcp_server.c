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
    struct sockaddr_in sa;
    int ret = 0;

    int socketFD = socket(PF_INET, SOCK_STREAM, IPPROTO_TCP);
    if (socketFD == -1)
    {
        perror("Can not  create socket");
        exit(EXIT_FAILURE);
    }

    memset(&sa, 0, sizeof(sa));

    sa.sin_family = AF_INET;
    sa.sin_port = htons(PORT);
    sa.sin_addr.s_addr = htonl(INADDR_ANY);

    ret = bind(socketFD, (struct sockaddr*)&sa, sizeof(sa));
    if (ret == -1)
    {
        perror("Bind failed");
        close(socketFD);
        exit(EXIT_FAILURE);
    }

    ret = listen(socketFD, 10);
    if (ret == -1)
    {
        perror("Listen failed");
        close(socketFD);
        exit(EXIT_FAILURE);
    }

    while (FOREVER)
    {
        int connectFD = accept(socketFD, NULL, NULL);

        if (connectFD < 0)
        {
            perror("Accept failed");
            close(connectFD);
            close(socketFD);
            exit(EXIT_FAILURE);
        }

        /* Do the RW here. */

        ret = shutdown(connectFD, SHUT_RDWR);
        if (ret < 0)
        {
            perror("Shutdown failed");
            close(connectFD);
            close(socketFD);
            exit(EXIT_FAILURE);
        }
    }

    return 0;
}