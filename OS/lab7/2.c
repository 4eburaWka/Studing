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
	char str[100];
	while(1){

		sleep(0.1);
		sem_wait(check);
		FILE* file = fopen("text", "r");
		fscanf(file, "%s", str);
		c = str[strlen(str)-1];
		fclose(file);
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
