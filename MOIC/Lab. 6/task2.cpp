// на C++ реализовать программу для нахождения компонента двусвязности неориентированного графа, задана матрица смежности
// программа должна выводить точки сочленения и мосты, и его компоненты двусвзности

#include <iostream>
#include <vector>
#include "..\graphs.h"
using namespace std;

void BFS(vector<vector<int>> &adjacencyMatrix, vector<int> &visited, int start=0)
{
    int max_node = adjacencyMatrix.size();
    queue q;
    q.push(start);
    while (!q.is_empty())
    {
        int v = q.front();
        q.pop();
        if (!visited[v])
        {
            visited[v] = 1;
            for (int i = 0; i < max_node; i++)
            {
                if (adjacencyMatrix[v][i] && !visited[i])
                {
                    q.push(i);
                }
            }
        }
    }
}

int conCompBFS(vector<vector<int>> &adjacencyMatrix)
{
    int max_node = adjacencyMatrix.size();
    int count = 0;
    vector<int> visited(max_node);
    for (int i = 0; i < max_node; i++)
    {
        visited[i] = 0;
    }
    for (int i = 0; i < max_node; i++)
    {
        if (!visited[i])
        {
            BFS(adjacencyMatrix, visited, i);
            count++;
        }
    }
    return count;
}

int main(){
    char path[] = "cons2";
    const int max_node = getTopsCount(path), EDGES = getEdgesCount(path);
    int **adjMatrix = adjacencyMatrixFromConnections(path);

    vector<vector<int>> adjacencyMatrix(max_node, vector<int>(max_node, 0));
    for (int i = 0; i < max_node; i++) {
        for (int j = 0; j < max_node; j++) {
            adjacencyMatrix[i][j] = adjMatrix[i][j];
        }
    }
    vector<vector<int>> bufferMatrix = adjacencyMatrix;

   	vector<int> visited(max_node);
    int count;
    count = conCompBFS(adjacencyMatrix);
    
    int k;
    vector<int> articulationPoints;
    for (int i = 0; i < max_node; i++)
    {
        for (int j = 0; j < bufferMatrix.size(); j++)
        {
            bufferMatrix[j].erase(bufferMatrix[j].begin() + i);
        }
        bufferMatrix.erase(bufferMatrix.begin() + i);

        k = conCompBFS(bufferMatrix);
        if (k > count)
        {
            articulationPoints.push_back(i);
        }
        bufferMatrix = adjacencyMatrix;
    }

    std::cout << "Articulation points: ";
    for (int i = 0; i < articulationPoints.size(); i++)
    {
        std::cout << articulationPoints[i] + 1 << " ";
    }

    vector<vector<int>> bridges;
    vector<int> vis(max_node);
    for (int i = 0; i < articulationPoints.size(); i++)
    {
        for (int j = 0; j < max_node; j++)
        {
            bufferMatrix[articulationPoints[i]][j] = 0;
            bufferMatrix[j][articulationPoints[i]] = 0;

            k = conCompBFS(bufferMatrix);
            if (k > count)
            {
                bridges.push_back( {articulationPoints[i], j} );
                vis[articulationPoints[i]] = 1;
                vis[j] = 1;
            }
            bufferMatrix = adjacencyMatrix;
        }
    }

    for (int i = 0; i < bridges.size(); i++)
    {
        for (int j = 0; j < bridges.size(); j++)
        {
            if (bridges[i][0] == bridges[j][1] && bridges[i][1] == bridges[j][0])
            {
                bridges.erase(bridges.begin() + j);
            }
        }
    }

    std::cout << "\nBridges: ";
    for (int i = 0; i < bridges.size(); i++)
    {
        std::cout << "(" << bridges[i][0] + 1 << ", " << bridges[i][1] + 1 << ") ";
    }
    // вывести компоненты двусвязности
    std::cout << "\nComponents: " << count << endl;
    
}