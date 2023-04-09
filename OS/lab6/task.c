#include <stdio.h>
#include <stdlib.h>
#include <errno.h>
#include <unistd.h>
#include <fcntl.h>
#include <mqueue.h>
#include <string.h>

char findMax(int a, int b, int c){
    if (a > b && a > c) return '1';
    if (b > a && b > c) return '2';
    return '3';
}

int main(){
    mqd_t mqID;
    mqID = mq_open("/SendingStrings", O_RDWR | O_CREAT | O_EXCL, 0666, NULL);
    if (mqID < 0){
        if (errno == EEXIST){
            mq_unlink("/SendingStrings");
            mqID = mq_open("/SendingStrings", O_RDWR | O_CREAT | O_EXCL, 0666, NULL);
        } else {
            perror("open message queue error!\n");
            return -1;
        }
    }
    
    struct mq_attr mqAttr;
    mq_getattr(mqID, &mqAttr); 
    
    if (fork() == 0){
        char buf1[100], buf2[100], buf3[100];
        if (mq_receive(mqID, buf1, mqAttr.mq_msgsize, NULL) < 0){
            printf("receive message 1 failed... \n");
            perror("error info ");
        }
        if (mq_receive(mqID, buf2, mqAttr.mq_msgsize, NULL) < 0){
            printf("receive message 2 failed... \n");
            perror("error info ");
        }
        if (mq_receive(mqID, buf3, mqAttr.mq_msgsize, NULL) < 0){
            printf("receive message 3 failed... \n");
            perror("error info ");
        }
        char s = findMax(strlen(buf1), strlen(buf2), strlen(buf3));
        if (mq_send(mqID, &s, sizeof(s), 1) < 0)
            printf("message 4 not sended.\n");
        exit(0);
    }
    
    FILE * file=fopen("strings", "r");
    
    
    char str1[50], str2[50], str3[50];
    fgets(str1, 50, file);
    fgets(str2, 50, file);
    fgets(str3, 50, file);
    if (mq_send(mqID, str1, sizeof(str1), 4) < 0)
        printf("message 1 not sended.\n");
    if (mq_send(mqID, str2, sizeof(str2), 3) < 0)
        printf("message 2 not sended.\n");
    if (mq_send(mqID, str3, sizeof(str2), 2) < 0)
        printf("message 3 not sended.\n");
         
    sleep(1);
    char a;
    if (mq_receive(mqID, &a, mqAttr.mq_msgsize, NULL) < 0){
        printf("receive message 4 failed... \n");
        perror("error info ");
    } else printf("The string %c is the longest.\n", a);
    fclose(file);
}
