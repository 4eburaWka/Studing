#include <unistd.h>
#include <sys/types.h>
#include <stdio.h>
#include <stdlib.h>

int main(){
    pid_t pid;
    
    printf("PID: %d, PPID: %d\n", getpid(), getppid());
    
    
    if ((pid = fork()) < 0){ // 2
        printf("ERROR:2\n");
        exit(1);
    }
    else if (pid == 0){
        printf("Proccess 2:%d was born by proccess %d.\n", getpid(), getppid());
        if ((pid = fork()) < 0){ // 3
            printf("ERROR:3\n");
            exit(1);
        }
        else if (pid == 0){
            printf("Proccess 3:%d was born by proccess %d.\n", getpid(), getppid());
            if ((pid = fork()) < 0){ // 5
                printf("ERROR:5\n");
                exit(1);
            }
            else if (pid == 0){
                printf("Proccess 5:%d was born by proccess %d.\n", getpid(), getppid());
                printf("Proccess 5:%d was closed. PPID : %d.\n", getpid(), getppid());
                exit(0);
            } else sleep(1);
            if ((pid = fork()) < 0){ // 7
                printf("ERROR:7\n");
                exit(1);
            }
            else if (pid == 0){
                printf("Proccess 7:%d was born by proccess %d.\n", getpid(), getppid());
                printf("Proccess 7:%d was closed. PPID : %d.\n", getpid(), getppid());
                exit(0);
            } else sleep(1);
            printf("Proccess 3:%d was closed. PPID : %d.\n", getpid(), getppid());
            exit(0);
        } else sleep(1);
        if ((pid = fork()) < 0){ // 4
            printf("ERROR:4\n");
            exit(1);
        }
        else if (pid == 0){
                    printf("Proccess 4:%d was born by proccess %d.\n", getpid(), getppid());
                    if ((pid = fork()) < 0){ // 6
                        printf("ERROR:6\n");
                        exit(1);
                    }
                    else if (pid == 0){
                        printf("Proccess 6:%d was born by proccess %d.\n", getpid(), getppid());
                        printf("Proccess 6:%d was closed. PPID : %d.\n", getpid(), getppid());
                        exit(0);
                    } else sleep(1);
                    printf("Proccess 4:%d was closed. PPID : %d.\n", getpid(), getppid());
                    exit(0);
        } else sleep(1);
        printf("Proccess 2:%d was closed. PPID : %d.\n", getpid(), getppid());
        exit(0);
    }
    
    execl("/bin/pwd", "pwd", "-P", NULL);
}//0122345
