#include <iostream>
#include <fstream>
#include "../graphs.h"
#define inf 1000000000
using namespace std;

int indexOfMin(int *list, int n){
    int min = inf;
    int index = -1;
    for(int i = 0; i < n; i++){
        if(list[i] < min){
            min = list[i];
            index = i;
        }
    }
    return index;
}
string toString(int num){
    if(num == 0) return "0";
    string str = "";
    while(num > 0){
        str = (char)(num % 10 + '0') + str;
        num /= 10;
    }
    return str;
}

void Dejkstra(int **graph, int tops, int vertex){
    int list[tops], distances[tops]; //string visited[6];
    bool STOP[tops];
    for (int i = 0; i < tops; i++){
        STOP[i] = false; // Флаг остановки
        list[i] = inf; // текущие расстояния от вершины до всех остальных
        distances[i] = 0;  // растояния с начальной вершнины до всех остальных
    }
    for (int x = 0; x < tops - 1; x++){
        STOP[vertex] = true;
        for(int i = 0; i < tops; i++){

            if (graph[vertex][i] + distances[vertex] < list[i] && !STOP[i]){
                list[i] = graph[vertex][i] + distances[vertex];
            }
        }
        list[vertex] = inf;
        vertex = indexOfMin(list, tops);
        distances[vertex] = list[vertex];
    }

    for (int i = 0; i < tops; i++){
        cout << distances[i] << "\t";
    }
    cout << endl;
}

void Floyd(int **graph, int tops, int vertex){
    int distances[tops][tops];
    for (int i = 0; i < tops; i++){
        for (int j = 0; j < tops; j++){
            distances[i][j] = graph[i][j];
        }
    }
    for (int k = 0; k < tops; k++){
        for (int i = 0; i < tops; i++){
            for (int j = 0; j < tops; j++){
                if (distances[i][k] + distances[k][j] < distances[i][j]){
                    distances[i][j] = distances[i][k] + distances[k][j];

                }
            }
        }
    }
    for (int i = 0; i < tops; i++){
        cout << distances[i][vertex] << "\t";
    }
    cout << endl;
}

int main(){
    char path[]= "cons.txt";
    const int tops = getTopsCount(path), edges = getEdgesCount(path);
    int **adjacencyMatrix = adjacencyMatrixFromConnectionsWithHeights(path);
    for (int i = 0; i < tops; i++)
    	for (int j = 0; j < tops; j++)
    		if (i != j && adjacencyMatrix[i][j] == 0)
    			adjacencyMatrix[i][j] = inf;
    
    Dejkstra(adjacencyMatrix, tops, 2);
    Floyd(adjacencyMatrix, tops, 2);
}
