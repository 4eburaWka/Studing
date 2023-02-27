#include "..\graphs.h"
#include <iostream>
using namespace std;

int find(int el, int* arr, int len){
    for (int i = 0; i < len; i++){
        if (arr[i] == el)
            return i;
    }
    return -1;
}

void dfs(int v, vector<vector<int>>& adj_matrix, vector<bool>& visited, list& res) {
    visited[v] = true; // помечаем вершину как посещенную
    res.append(v);
    for (int u = 0; u < adj_matrix.size(); u++) {
        if (adj_matrix[v][u] == 1 && !visited[u]) { // если есть ребро и вершина не посещена
            dfs(u, adj_matrix, visited, res); // рекурсивно вызываем dfs для смежной вершины
            res.append(v);
        }
    }
    
}

int main(){
    char path[] = "E:\\Studing\\MOIS\\Lab. 7\\cons";
    int tops = getTopsCount(path), edges = getEdgesCount(path);
    int** matr = adjacencyMatrixFromConnections(path);
    vector<vector<int>> adj(tops, vector<int> (tops));
    vector<bool> vis(tops, false);
    for (int i = 0; i < tops; i++)
        for (int j = 0; j < tops; j++) 
            adj[i][j] = matr[i][j]; 

    list dfs_res;
    dfs(0, adj, vis, dfs_res);

    // префиксный(прямой) обход
    list pref, pref_res;
    for (int i = 0; i < dfs_res.length; i++)
        pref.append(dfs_res.list[i]);
    for (int i = 0; i < dfs_res.length; i++){
        if (pref_res.find(pref.list[i]) != -1)
            continue;
        pref_res.append(pref.list[i]);
    }
    for (int i = 0; i < pref_res.length; i++)
        cout << pref_res.list[i] + 1 << " ";
    cout << endl;


    // инфиксный(симметричный) обход
    list inf, inf_res, meets; // в meet будут записаны вершины, которые встречались раньше 
    int temp;
    for (int i = 0; i < dfs_res.length; i++)
        inf.append(dfs_res.list[i]);
    for (int i = 0; i < dfs_res.length; i++){
        temp = inf.list[i];
        if (meets.find(temp) != -1 && inf_res.find(temp) == -1)
            inf_res.append(temp);
        meets.append(inf.list[i]);
        inf.list[i] = -1;
        if (inf.find(temp) == -1 && inf_res.find(temp) == -1)
            inf_res.append(temp);
    }
    for (int i = 0; i < inf_res.length; i++)
        cout << inf_res.list[i] + 1 << " ";
    cout << endl;


    // постфиксный(обратный) обход
    list postf, postf_res; // в meet будут записаны вершины, которые встречались раньше
    for (int i = 0; i < dfs_res.length; i++)
        postf.append(dfs_res.list[i]);
    for (int i = 0; i < dfs_res.length; i++){
        temp = postf.list[i];
        postf.list[i] = -1;
        if (postf.find(temp) == -1)
            postf_res.append(temp);
    }
    for (int i = 0; i < postf_res.length; i++)
        cout << postf_res.list[i] + 1 << " ";
    cout << endl;
}