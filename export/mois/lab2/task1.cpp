#include <iostream>  
using namespace std;



class stack{
    public:
        int length=0;
        int stack[100];
        int get(){
            return stack[length-- - 1];
        }
        void add(int num){
            stack[length++] = num;
        }
        int check(){
            return stack[length-1];
        }
};
class queue{
    public:
        int q[100];
        int length = 0, left = 0, right = 0;
        void add(int num){
            q[right++] = num; length++;
        }
        int get(){
            length--;
            return q[left++];
        }
        void swap(int pos1, int pos2){
            int t = q[pos1];
            q[pos1] = q[pos2];
            q[pos2] = t;
        }
};
class list{
    public:
        int list[100];
        int length=0;
        void append(int num){
            list[length++] = num;
        }
        int last(){
            return list[length-1];
        }

};

bool isVertexHasNeighbors(int (*graph)[5], int vertex){
    for (int i = 0; i < 5; i++){
        if (graph[vertex][i] == 1)
            return true;
    }
    return false;
}

// ############################################################
void findEulerianCycle(int (*matrix)[5], int vertex){
    int graph[5][5];
    for (int i = 0; i < 5; i++){
        for (int j = 0; j < 5; j++){
            graph[i][j] = matrix[i][j];
        }
    }
    
    stack S;
    list C;

    S.add(vertex);

    while (true){
        if (!isVertexHasNeighbors(graph, S.check()))
            {C.append(S.get()); vertex = S.check();}
        else {
            for (int i = 0; i < 5; i++){
                if (graph[vertex][i] == 1){
                    graph[vertex][i] = 0; graph[i][vertex] = 0; 
                    S.add(i); vertex = i; break;
                }
            }
        }
        if (C.list[0] == C.last() and C.length>1){
            for (int i = 0; i < C.length; i++)
                cout << C.list[i]+1;
            cout << endl;
            break;
        }
    }
}
// ############################################################

void findGamiltonCycle(int (*matrix)[9], int vertex){
    queue Q;
    list C;

    for (int i = 0; i < 9; i++){
        Q.add(i);
    }

    int i;
    for (int j = 0; j < 9 * 8; j++){
        if (matrix[Q.q[0]][Q.q[1]] != 1){
            i = 1;
            while (matrix[Q.q[0]][Q.q[i]] != 1 || matrix[Q.q[1]][Q.q[i+1]] != 1){
                i++;
            }
            for (int k = 0; 1 + k < i - k; k++){
                Q.swap(1 + k, i - k);
            }
            Q.add(Q.get());
        }
    }
    for (i = 0; i < 9; i++)
        cout << Q.q[i];
    cout << endl;
}
// ############################################################

int main() {
    const int tops1 = 5, edges1 = 10;
    int adjacencyMatrix1[tops1][tops1] = {{0, 1, 1, 1, 1},
                                          {1, 0, 1, 1, 1},
                                          {1, 1, 0, 1, 1},
                                          {1, 1, 1, 0, 1},
                                          {1, 1, 1, 1, 0}};
    
    findEulerianCycle(adjacencyMatrix1, 0);

    const int tops2 = 9, edges2 = 12;
    int adjacencyMatrix2[tops2][tops2] = {{0, 1, 0, 0, 0, 0, 1, 0, 0},
                                          {1, 0, 0, 1, 0, 0, 0, 1, 1},
                                          {0, 0, 0, 1, 1, 0, 0, 0, 0},
                                          {0, 1, 1, 0, 0, 1, 0, 0, 0},
                                          {0, 0, 1, 0, 0, 1, 1, 0, 0},
                                          {0, 0, 0, 1, 1, 0, 0, 1, 0},
                                          {1, 0, 0, 0, 1, 0, 0, 0, 0},
                                          {0, 1, 0, 0, 0, 1, 0, 0, 1},
                                          {0, 1, 0, 0, 0, 0, 0, 1, 0}};
    
    findGamiltonCycle(adjacencyMatrix2, 0);
}