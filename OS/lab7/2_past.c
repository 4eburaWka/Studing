#include <semaphore.h>
#include <fcntl.h>
#include <stdio.h>
#include <string.h>
#include <unistd.h>
int main(){
 sem_t *input;
 sem_t *check;
 const char *sem_input = "input";
 const char *sem_check = "check";
 input = sem_open(sem_input, O_CREAT, 0777, 1);
 check = sem_open(sem_check, O_CREAT, 0777, 0);
 char c;
 short j;
 while(1){
  sem_wait(check);
  FILE* file = fopen("text", "r");zz
  j = fread(&c, sizeof(char), 1, file);
  fclose(file);
  if(j) 
   printf("%c\n", c);
  if(c == 'q'){
   printf("End of process->%c.\n", c); 
   break;
  }
  sem_post(input);
 }
 sem_close(input);
 sem_close(check);
 sem_unlink(sem_input);
 sem_unlink(sem_check);
}
