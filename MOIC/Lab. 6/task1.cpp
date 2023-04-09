#include <iostream>
#include <vector>
#include "graph_LIB.hh"
using namespace std;

// транспонировать матрицу
// входные данные: матрица смежности, количество вершин
// выходные данные: транспонированная матрица
vector<vector<int>> transposeMatrix(vector<vector<int>> &matrix, int n) {
    vector<vector<int>> transposedMatrix(n, vector<int>(n, 0));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            transposedMatrix[i][j] = matrix[j][i];
        }
    }
    return transposedMatrix;
}

// поиск в глубину
// входные данные: номер вершины, матрица смежности, вектор посещенных вершин, вектор порядка обхода
// cout
void dfs1(int v, vector<vector<int>> &matrix, vector<int> &visited, vector<int> &order) {
    visited[v] = 1;
    for (int i = 0; i < matrix[v].size(); i++) {
        if (matrix[v][i] && !visited[i]) {
            dfs1(i, matrix, visited, order);
        }
    }
    order.push_back(v);
}

// поиск в глубину
// входные данные: номер вершины, матрица смежности, вектор посещенных вершин, номер компоненты
// cout
void dfs2(int v, vector<vector<int>> &matrix, vector<int> &visited, int componentNumber) {
    visited[v] = componentNumber + 1;
    for (int i = 0; i < matrix[v].size(); i++) {
        if (matrix[v][i] && !visited[i]) {
            dfs2(i, matrix, visited, componentNumber);
        }
    }
}

// найти компонент сильной связности орграфа
// входные данные: матрица смежности, количество вершин
// cout
void findStronglyConnectedComponents(vector<vector<int>> &matrix, int n) {
    vector<int> visited(n, 0);
    vector<int> order;
    for (int i = 0; i < n; i++) {
        if (!visited[i]) {
            dfs1(i, matrix, visited, order);
        }
    }
    vector<vector<int>> transposedMatrix = transposeMatrix(matrix, n);
    vector<int> component(n, 0);
    int componentNumber = 0;
    for (int i = n - 1; i >= 0; i--) {
        if (!component[order[i]]) {
            dfs2(order[i], transposedMatrix, component, componentNumber);
            componentNumber++;
        }
    }
    cout << "Strongly connected component: " << componentNumber << endl;
    cout << "Components: " << endl;
    for (int i = 0; i < componentNumber; i++) {
        cout << i + 1 << ": ";
        for (int j = 0; j < n; j++) {
            if (component[j] == i + 1) {
                cout << j + 1 << " ";
            }
        }
        cout << endl;
    }
}




int main(){
    convert c;
	std::string file_path = "cons.txt";
	std::vector<int> nodes = c.reading_file(file_path);
	
    const int TOPS = c.count_of_nodes(nodes);
	std::vector<std::vector<int>> adjMatrix = c.oriented_adjancy(nodes, TOPS);
    const int EDGES = nodes.size()/2;
    


    vector<vector<int>> graph(TOPS, vector<int>(TOPS, 0));
	for (int i = 0; i < TOPS; i++) {
		for (int j = 0; j < TOPS; j++) 
			graph[i][j] = adjMatrix[i][j];
	}

    findStronglyConnectedComponents(graph, TOPS);

}
