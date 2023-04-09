#include <stdio.h>

void DFS(int s, int max_tops, int *matrx[], char *used){//подсчёт числа компонент связности с
    used[s] = 1;                                     //помощью поиска в глубину
    for (int i = 0; i < max_tops; i++) {
        if (used[i] == 0 && matrx[s-1][i-1] == 1)
            DFS(i, max_tops,matrx , used);
    }
}



int main(){
    int max_tops = 8;
    int graph[8][8] = {{0, 1, 1, 0, 0, 0, 0, 0},
                       {1, 0, 1, 0, 0, 0, 0, 0},
                       {1, 1, 0, 1, 1, 0, 0, 0},
                       {0, 0, 1, 0, 1, 0, 0, 0},
                       {0, 0, 1, 1, 0, 1, 0, 0},
                       {0, 0, 0, 0, 1, 0, 0, 0},
                       {0, 0, 0, 0, 0, 0, 0, 1},
                       {0, 0, 0, 0, 0, 0, 1, 0}};
    char used[max_tops];
    int *buf[max_tops], cnt = 0;

    for(int i = 0; i < max_tops; i++){//цикл для получения возможности передачи двумерного
        buf[i]=graph[i]; //массива в функцию
    }
    
    DFS(2,max_tops,buf,used);
    for (int i = 0; i < max_tops; i++) {
        if (used[i] == 0) {
            DFS(i, max_tops, buf, used);
            cnt++;
        }
    }
    printf("%d", cnt);

    return 0;
}