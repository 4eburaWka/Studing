#include <iostream>  
#include "../graphs.h"
using namespace std;


bool isVertexHasNeighbors(int **graph, int TOPS, int vertex){
    for (int i = 0; i < TOPS; i++){
        if (graph[vertex][i] == 1)
            return true;
    }
    return false;
}
int bfs(int **graph, int vertex, int n){
    bool visited[n], available[n], run = true;
    for (int i = 0; i < n; i++)
        visited[i] = available[i] = false;
    
    int number = 0;
    while(run){
        available[vertex] = visited[vertex] = true;
        for (int c = 0; c < n; c++){
            for (int i = 0; i < n; i++){
                if (graph[vertex][i])
                    available[i] = true;
            }
            for (int i = 0; i < n; i++){
                if (available[i] && !visited[i])
                    {vertex = i; visited[i] = true; break;}
            }
        }
        number++;
        
        for (int i = 0; i < n; i++){
                if(!visited[i]) {vertex = i; run = true; break;}
                else run = false;
        }
    }
    return number;
}
bool ischetko(int **matrix, int n){
    int count;
    for (int i = 0; i < n; i++){
        count = 0;
        for (int j = 0; j < n; j++){
            count += matrix[i][j];
        }
        if (count % 2 == 1)
            return false;
    }
    return true;
}
// ############################################################
void findEulerianCycle(int **matrix, int vertex, int edges, const int n){
    if (bfs(matrix, vertex, n) == 1 && ischetko(matrix, n)){
        int **graph;
        graph = new int*[n];
        for (int i = 0; i < n; i++)
            graph[i] = new int[n];
        for (int i = 0; i < n; i++){
            for (int j = 0; j < n; j++){
                graph[i][j] = matrix[i][j];
            }
        }
        
        stack S;
        list C;

        S.add(vertex);

        while (true){
            if (!isVertexHasNeighbors(graph, n, S.check()))
                {C.append(S.get()); vertex = S.check();}
            else {
                for (int i = 0; i < n; i++){
                    if (graph[vertex][i] == 1){
                        graph[vertex][i] = 0; graph[i][vertex] = 0; 
                        S.add(i); vertex = i; break;
                    }
                }
            }
            if (C.length == edges + 1){
                for (int i = 0; i < C.length; i++)
                    cout << C.list[i] + 1;
                cout << endl;
                break;
            }
        }
    }
}
// ############################################################

void findGamiltonCycle(int **matrix, int vertex, int n){
    queue Q;

    for (int i = 0; i < n; i++){
        Q.add(i);
    }

    int i;
    for (int j = 0; j < n * (n-1); j++){
        if (matrix[Q.q[0]][Q.q[1]] != 1){
            i = 1;
            while (matrix[Q.q[0]][Q.q[i]] != 1 || matrix[Q.q[1]][Q.q[i+1]] != 1){
                i++;
            }

            Q.swap(1, i);
            
            Q.add(Q.get());
        }
    }
    for (i = 0; i < n; i++)
        cout << Q.q[i];
    cout << endl;
}
// ############################################################

int main() {
    char path[] = "cons";
    const int tops1 = getTopsCount(path), edges1 = getEdgesCount(path);
    int **adjacencyMatrix1 = adjacencyMatrixFromConnections(path);
    /*for(int i =0;i<tops1;i++){
    	for (int j=0;j<tops1;j++)
    		cout << adjacencyMatrix1[i][j] << " ";
    	cout << endl;
	}*/
    
    findEulerianCycle(adjacencyMatrix1, 0, edges1, tops1);

    char path2[] = "cons2";
    const int tops2 = getTopsCount(path2), edges2 = getEdgesCount(path2);
    int **adjacencyMatrix2 = adjacencyMatrixFromConnections(path2);
    /*for(int i =0;i<tops1;i++){
    	for (int j=0;j<tops1;j++)
    		cout << adjacencyMatrix2[i][j] << " ";
    	cout << endl;
	}*/
    
    findGamiltonCycle(adjacencyMatrix2, 0, tops2);
}
