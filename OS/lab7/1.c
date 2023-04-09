#include <stdio.h>
#include <pthread.h>
#include<string.h>
#include<stdlib.h>
int main()
{ 
    int pthread_mutex_init(pthread_mutex_t *mutex, const pthread_mutexattr_t *attr);
    FILE*file;
    //char symb;
    char str[256];
    int k=0;
    while(k<1)
    {
        int pthread_mutex_lock(pthread_mutex_t *mutex);
        file = fopen("1.txt","r");
   
  while (fgets(str,255, file) != 0){}
  printf("Строка %s \n",str);
  int p=strlen(str);
  printf("Количество символов %d ", p);
        int pthread_mutex_unlock(pthread_mutex_t *mutex);
k++;
    }
        
}
