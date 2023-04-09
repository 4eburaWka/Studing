#include <set>
#include <iostream>
#include <cstring>
#include <vector>
#include <algorithm>
#include "../graphs.h"

#define INF 1000000000

using namespace std;

void PRIMA(int **graph, int tops){ 
	int selected[tops]; 
	memset(selected, false, sizeof(selected));

	int no_edge = 0; 
	int x, y;
	while (no_edge < tops) { 
		int min = INF;
		x = 0;
		y = 0;

		for (int i = 0; i < tops; i++) {
			if (selected[i]) {
				for (int j = 0; j < tops; j++) {
					if (!selected[j] && graph[i][j]) {
						if (min > graph[i][j]) {
							min = graph[i][j];
							x = i;
							y = j;
						}
					}
				}
			}
		}
		cout << x + 1 <<  " - " << y + 1 << " :  " << graph[x][y];
		cout << endl;
		selected[y] = true;
		no_edge++;
    }
}

void KRUSKAL(std::vector<std::vector<int>> &adjacencyMatrix){ 
	int max_node = adjacencyMatrix.size(); 
	std::vector<std::vector<int>> distance(max_node, std::vector<int>(max_node, INF)); 
	std::vector<std::vector<int>> tree(max_node, std::vector<int>(max_node, 0)); 
	std::vector<std::vector<int>> edges; 
	for (int i = 0; i < max_node; i++){ 
		for (int j = 0; j < max_node; j++){ 
			if (adjacencyMatrix[i][j] != 0){ 
				edges.push_back({ adjacencyMatrix[i][j], i, j }); 
			} 
		} 
	} 
	std::sort(edges.begin(), edges.end()); 
	std::vector<int> tree_id(max_node); 
	for (int i = 0; i < max_node; i++){ 
		tree_id[i] = i; 
	} 
	for (int i = 0; i < edges.size(); i++){ 
		int cost = edges[i][0]; 
		int a = edges[i][1]; 
		int b = edges[i][2]; 
		if (tree_id[a] != tree_id[b]){ 
			tree[a][b] = cost; 
			tree[b][a] = cost; 
			int old_id = tree_id[b]; 
			int new_id = tree_id[a]; 
			for (int j = 0; j < max_node; j++){ 
				if (tree_id[j] == old_id){ 
					tree_id[j] = new_id; 
				} 
			} 
		} 
	} 
	for(int i = 0; i < max_node; i++)
		for(int j = i; j < max_node; j++)
			if(tree[i][j] != 0) 
				cout << i + 1 << " - " << j + 1 << " : " << tree[i][j] << endl; 
}

int main(){
    char path[] = "cons";
    const int TOPS = getTopsCount(path), EDGES = getEdgesCount(path);
    int **adjacencyMatrix = adjacencyMatrixFromConnectionsWithHeights(path);

	vector<vector<int>> graph(TOPS, vector<int>(TOPS, 0));
	for (int i = 0; i < TOPS; i++) {
		for (int j = 0; j < TOPS; j++) {
			graph[i][j] = adjacencyMatrix[i][j];
			cout << graph[i][j] << " ";
		}
		cout << endl;
	}

	cout << "Prim's algorithm:" << endl;
	PRIMA(adjacencyMatrix, TOPS);

	cout << endl << "Kruskal's algorithm:" << endl;
	KRUSKAL(graph);
}
