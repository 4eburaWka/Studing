#include <stdio.h>
#include <stdbool.h>

int bfs(int (*graph)[8], int vertex){
    bool visited[8], available[8], run = true;
    for (int i = 0; i < 8; i++)
        visited[i] = available[i] = false;
    
    int number = 0;
    while(run){
        available[vertex] = visited[vertex] = true;
        for (int c = 0; c < 8; c++){
            for (int i = 0; i < 8; i++){
                if (graph[vertex][i])
                    available[i] = true;
            }
            for (int i = 0; i < 8; i++){
                if (available[i] && !visited[i])
                    {vertex = i; visited[i] = true; break;}
            }
        }
        number++;
        
        for (int i = 0; i < 8; i++){
                if(!visited[i]) {vertex = i; run = true; break;}
                else run = false;
        }
    }
    return number;
}
int main(){
    int graph[8][8] = {{0, 0, 0, 1, 0, 0, 0, 0},
                       {0, 0, 0, 1, 0, 1, 0, 0},
                       {0, 0, 0, 0, 0, 1, 0, 0},
                       {1, 1, 0, 0, 1, 0, 0, 0},
                       {0, 0, 0, 1, 0, 1, 0, 0},
                       {0, 1, 1, 0, 1, 0, 0, 0},
                       {0, 0, 0, 0, 0, 0, 0, 1},
                       {0, 0, 0, 0, 0, 0, 1, 0}};
    printf("%d", bfs(graph,0));
}