#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <fstream>
#include <algorithm>
#include <stack>

#define inf 2147483647

class Stack{
private:
    std::vector <int> array;
    int head = -1;
public:
    void push(int x) 
    {
        head++;
        array.push_back(x);
    }

    void pop()
    {
        head--;
        array.pop_back();        
    }

    int front()
    {
        return array[head];
    }

    bool is_empty()
    {
        return head == -1;
    }

    void print()
    {
        int l = array.size();
        for (int i = 0; i < l; i++)
        {
            std::cout << array[i]<<"-";
        }
        std::cout << std::endl;
    }
    
    int operator[](int i)
    {
        return array[array.size() - i - 1];
    }
};

class queue
{
private:
    std::vector <int> array;
    int tail = 0; 
public:
    void push(int x) 
    {
        array.push_back(x);
        tail++;
    }

    void pop() 
    {
        array.erase(array.cbegin());
        tail--;
    }

    int front()
    {
        return array[0];
    }

    bool is_empty() 
    {
        return tail == 0;
    }

    int size(){
        int count = 0;
        for (int i = 0; i < tail; i++)
        {
            count++;
        }
        return count;
    }
    void print()
    {
        int l = array.size();
        for (int i = 0; i < l; i++)
        {
            std::cout << array[i]+1<<"-";
        }
        std::cout << std::endl;
    }

    void swap(int i, int j)
    {
        int temp = array[i];
        array[i] = array[j];
        array[j] = temp;
    }
    

    int operator[](int i)
    {
        return array[i];
    }
};

class convert{
public:
    static std::vector<int> reading_file(std::string file_cycle) 
    {
        std::ifstream fin; 
        fin.open(file_cycle); 
        std::string first_str; 
        for (int i=0; ;i++){ 
            getline(fin,first_str); 
            if (fin.fail()) 
                std::cout<<"fail"<<std::endl;
                break; 
            }
        std::string newstr;
        std::string delet;
        delet = ",";
        newstr = "";
        std::vector<std::string> array_newstr;
        std::vector<int> rebro_int_array;

        int size_str;
        size_str = first_str.size();

        for(int i=0;i<size_str;i++){
            if(first_str[i]!='(' && first_str[i]!=')'){
                newstr+=first_str[i];
            }
        }
        size_t beg, pos = 0;
        while ((beg = newstr.find_first_not_of(delet, pos)) != std::string::npos){                                                                  
            pos = newstr.find_first_of(delet, beg + 1);                  
            array_newstr.push_back(newstr.substr(beg, pos - beg));
        }
        for (auto & i : array_newstr)
            rebro_int_array.push_back(stoi(i));

        return rebro_int_array;
    } 

    int count_of_nodes(std::vector<int> nodes) {
	    int max_node = *max_element(nodes.begin(), nodes.end());
        return max_node;
    }
   
    std::vector<std::vector<int>> adjancy(std::vector<int> nodes, int max_node)
    {
	    int n = nodes.size() / 2, m = 2;
	    std::vector<std::vector<int>> array_edge(n, std::vector<int>(m));
        std::vector<std::vector<int>> array_edjancy(max_node, std::vector<int>(max_node));

	    for (int i = 0, j = 0; i < n, j < 2 * n; i++, j+=2){
	    	array_edge[i][0] = nodes[j];
	    }
	    for (int i = 0, j = 1; i < n, j < 2 * n; i++, j+=2){
	    	array_edge[i][1] = nodes[j];
	    }
        for (int i = 0; i < max_node; i++){
            for (int j = 0; j < max_node; j++){
                array_edjancy[i][j] = 0;
            }
        }
        for (int i = 0; i < n; i++){
            int x = array_edge[i][0];
            int y = array_edge[i][1];

            array_edjancy[x-1][y-1] = 1;
            array_edjancy[y-1][x-1] = 1;
        }
        return array_edjancy;
    }
    std::vector<std::vector<int>> oriented_adjancy(std::vector<int> nodes, int max_node)
    {
	    int n = nodes.size() / 2, m = 2;
	    std::vector<std::vector<int>> array_edge(n, std::vector<int>(m));
        std::vector<std::vector<int>> array_edjancy(max_node, std::vector<int>(max_node));

	    for (int i = 0, j = 0; i < n, j < 2 * n; i++, j+=2){
	    	array_edge[i][0] = nodes[j];
	    }
	    for (int i = 0, j = 1; i < n, j < 2 * n; i++, j+=2){
	    	array_edge[i][1] = nodes[j];
	    }
        for (int i = 0; i < max_node; i++){
            for (int j = 0; j < max_node; j++){
                array_edjancy[i][j] = 0;
            }
        }
        for (int i = 0; i < n; i++){
            int x = array_edge[i][0];
            int y = array_edge[i][1];

            array_edjancy[x-1][y-1] = 1;
            
        }
        return array_edjancy;
    }



    //если флаг равен 1 то матрица смежности весов сделана для алгоритма Дейкстры
    //если флаг равен 0 то матрица смежности весов сделана для алгоритма Флойда-Уоршелла
    std::vector<std::vector<int>> adjancy_for_deikstra_floid(std::vector<int> nodes,std::vector<int> weight, int max_node,int flag=1)
    {                                                       
	    int n = nodes.size() / 2, m = 2;
	    std::vector<std::vector<int>> array_edge(n, std::vector<int>(m));
        std::vector<std::vector<int>> array_edjancy(max_node, std::vector<int>(max_node));

	    for (int i = 0, j = 0; i < n, j < 2 * n; i++, j+=2){
	    	array_edge[i][0] = nodes[j];
	    }
	    for (int i = 0, j = 1; i < n, j < 2 * n; i++, j+=2){
	    	array_edge[i][1] = nodes[j];
	    }
        for (int i = 0; i < max_node; i++){
            for (int j = 0; j < max_node; j++){
                if(flag==1){
                    array_edjancy[i][j] = 0;
                }
                else{
                    if(i==j){
                        array_edjancy[i][j] = 0;
                    }
                    else{
                        array_edjancy[i][j] = inf;
                    }
                }
        }
        }
        for (int i = 0; i < n; i++){
            int x = array_edge[i][0];
            int y = array_edge[i][1];

            array_edjancy[x-1][y-1] = weight[i];
            array_edjancy[y-1][x-1] = weight[i];
           
        }
        return array_edjancy;
    }



    std::vector<std::vector<int>> incidence(std::vector<int> nodes, int max_node){   
        int n = nodes.size() / 2, m = 2;
	    std::vector<std::vector<int>> array_edge(n, std::vector<int>(m));
        std::vector<std::vector<int>> array_inciden(max_node, std::vector<int>(n));

	    for (int i = 0, j = 0; i < n, j < 2 * n; i++, j+=2){
	    	array_edge[i][0] = nodes[j];
	    }
	    for (int i = 0, j = 1; i < n, j < 2 * n; i++, j+=2){
	    	array_edge[i][1] = nodes[j];
	    }
	    for (int i = 0; i < max_node; i++){
	    	for (int j = 0; j < n; j++)
	    	{
	    		array_inciden[i][j] = 0;
	    	}
	    }
	    for (int i = 0; i < n; i++){
	    	array_inciden[array_edge[i][0] - 1][i] = 1;
	    	array_inciden[array_edge[i][1] - 1][i] = 1;
	    }
        return array_inciden;
    }
};

class alg{
public:
        int find_component_with_bfc(std::vector<std::vector<int>>adj){

            std::vector<int> used(adj.size()-1,0);
            int target=0;
            int count_of_components=0;
           

            for(bool i:used){
                if(i==0){
                    bfs(adj,used,target);
                    count_of_components++;
                }
                target++;
            }
            return count_of_components;
        }
        void bfs(std::vector<std::vector<int>>adj, std::vector<int> &used,int s) {
            std::vector<int> graph[adj.size()];
            for (int i = 0; i < adj.size(); ++i) {
                for (int j = 0; j < adj.size(); ++j) {
                    if (adj[i][j] == 1) {
                        graph[i].push_back(j);
                    }
                }
            }
            
            queue q;
            q.push(s);
            if (used[s]!=1){
                used[s] = true;
            }
           
            while (!q.is_empty()) {
                int v = q.front();
                q.pop();
                for (size_t i = 0; i < graph[v].size(); ++i) {
                    int to = graph[v][i];
                    if (!used[to]) {
                        used[to] = true;
                        q.push(to);
                    }
                }
            }
        }

    void DFS(std::vector<std::vector<int>> &adjacencyMatrix, std::vector<int> &visited, int start=0)
    {
        int max_node = adjacencyMatrix.size();
        Stack s;
        s.push(start);
        while (!s.is_empty())
        {
            int v = s.front();
            s.pop();
            if (!visited[v])
            {
                visited[v] = 1;
                for (int i = 0; i < max_node; i++)
                {
                    if (adjacencyMatrix[v][i] && !visited[i])
                    {
                        s.push(i);
                    }
                }
            }
        }
    }
    int conCompDFS(std::vector<std::vector<int>> &adjacencyMatrix)
    {
        int max_node = adjacencyMatrix.size();
        int count = 0;
        std::vector<int> visited(max_node);
        for (int i = 0; i < max_node; i++)
        {
            visited[i] = 0;
        }
        for (int i = 0; i < max_node; i++)
        {
            if (!visited[i])
            {
                DFS(adjacencyMatrix, visited, i);
                count++;
            }
        }
        return count;
    }
    queue Hamilton_cycle(std::vector<std::vector<int>> &array_edjancy)
    {
        int max_node = array_edjancy.size();
        queue q;
        for (int i = 0; i < max_node; i++)
        {
            q.push(i);
        }
        int i;
        for (int k = 0; k < max_node * (max_node - 1); k++)
        {
            if (array_edjancy[q[0]][q[1]] != 1)
            {
                i = 1;
                while (array_edjancy[q[0]][q[i]] != 1 || array_edjancy[q[1]][q[i + 1]] != 1) 
                {
                    i++;
                }
                for (int j = 0; 1 + j < i - j; j++)
                {
                    q.swap(1 + j, i - j);
                }
            }

            q.push(q.front());
            q.pop();
        }
        return q;
    }

    std::vector<int> euler(std::vector<std::vector<int>> &adjacencyMatrix, int poz=0)
    {
        int max_node = adjacencyMatrix.size();
        
        std::vector<int> path;
        Stack s;
        s.push(poz);
        while(!s.is_empty())
        {
            poz = s.front();
            bool temp = false;
            for (int i = 0; i < max_node; i++)
            {
                if (adjacencyMatrix[poz][i])
                {
                    adjacencyMatrix[poz][i] = 0;
                    adjacencyMatrix[i][poz] = 0;
                    s.push(i);
                    temp = true;
                    break;
                    
                }
            }
            if (!temp)
            {
                path.push_back((poz+1));
                s.pop();
            }
            
        }
        
        return path;
    }
    std::vector<int> deikstra(std::vector<std::vector<int>> &adjacencyMatrix, int start)
    {
        int max_node = adjacencyMatrix.size();
        std::vector<int> distance(max_node, inf);
        std::vector<int> visited(max_node, 0);
        distance[start] = 0;
        for (int i = 0; i < max_node; i++)
        {
            int v = -1;
            for (int j = 0; j < max_node; j++)
            {
                if (!visited[j] && (v == -1 || distance[j] < distance[v]))
                {
                    v = j;
                }
            }
            if (distance[v] == inf)
            {
                break;
            }
            visited[v] = 1;
            for (int j = 0; j < max_node; j++)
            {
                if (adjacencyMatrix[v][j] != 0)
                {
                    int to = j;
                    int len = adjacencyMatrix[v][j];
                    if (distance[v] + len < distance[to])
                    {
                        distance[to] = distance[v] + len;
                    }
                }
            }
        }
        return distance;
    }
    std::vector<std::vector<int>> floyd(std::vector<std::vector<int>> &adjacencyMatrix)
    {
        int max_node = adjacencyMatrix.size();
        std::vector<std::vector<int>> distance(max_node, std::vector<int>(max_node, inf));
        for (int i = 0; i < max_node; i++){
            for (int j = 0; j < max_node; j++){
                distance[i][j] = adjacencyMatrix[i][j];
            }
        }
        for (int k = 0; k < max_node; k++){
            for (int i = 0; i < max_node; i++){
                for (int j = 0; j < max_node; j++){
                    if (distance[i][k] < inf && distance[k][j] < inf){
                        distance[i][j] = std::min(distance[i][j], distance[i][k] + distance[k][j]);
                    }
                }
            }
        }
        return distance;
    }
    void prima(std::vector<std::vector<int>> &adjacencyMatrix)
    {
        int max_node = adjacencyMatrix.size();
        std::vector<std::vector<int>> distance(max_node, std::vector<int>(max_node, inf));
        std::vector<int> selected(max_node, 0);
        int no_edge = 0;
        selected[0] = 1;
        while (no_edge < max_node - 1)
        {
            int min = inf;
            int x = 0, y = 0;
            for (int i = 0; i < max_node; i++)
            {
                if (selected[i])
                {
                    for (int j = 0; j < max_node; j++)
                    {
                        if (!selected[j] && adjacencyMatrix[i][j])
                        {
                            if (min > adjacencyMatrix[i][j])
                            {
                                min = adjacencyMatrix[i][j];
                                x = i;
                                y = j;
                            }
                        }
                    }
                }
            }
            std::cout<<x+1<<" - "<<y+1<<" : "<<adjacencyMatrix[x][y]<<std::endl;
            selected[y] = 1;
            no_edge++;
        }
    }
   
    std::vector<std::vector<int>> kruskal(std::vector<std::vector<int>> &adjacencyMatrix)
    {
        int max_node = adjacencyMatrix.size();
        std::vector<std::vector<int>> distance(max_node, std::vector<int>(max_node, inf));
        std::vector<std::vector<int>> tree(max_node, std::vector<int>(max_node, 0));
        std::vector<std::vector<int>> edges;
        for (int i = 0; i < max_node; i++)
        {
            for (int j = 0; j < max_node; j++)
            {
                if (adjacencyMatrix[i][j] != 0)
                {
                    edges.push_back({ adjacencyMatrix[i][j], i, j });
                }
            }
        }
        std::sort(edges.begin(), edges.end());
        std::vector<int> tree_id(max_node);
        for (int i = 0; i < max_node; i++)
        {
            tree_id[i] = i;
        }
        for (int i = 0; i < edges.size(); i++)
        {
            int cost = edges[i][0];
            int a = edges[i][1];
            int b = edges[i][2];
            if (tree_id[a] != tree_id[b])
            {
                tree[a][b] = cost;
                tree[b][a] = cost;
                int old_id = tree_id[b];
                int new_id = tree_id[a];
                for (int j = 0; j < max_node; j++)
                {
                    if (tree_id[j] == old_id)
                    {
                        tree_id[j] = new_id;
                    }
                }
            }
        }
        return tree;
    }
    std::vector<std::vector<int>> kosaraju(std::vector<std::vector<int>> &adjacencyMatrix){
        int max_node = adjacencyMatrix.size();
        std::vector<std::vector<int>> distance(max_node, std::vector<int>(max_node, inf));
        std::vector<std::vector<int>> reverse(max_node, std::vector<int>(max_node, 0));
        std::vector<int> visited(max_node, 0);
        std::vector<int> order;
        for (int i = 0; i < max_node; i++){
            for (int j = 0; j < max_node; j++){
                reverse[j][i] = adjacencyMatrix[i][j];
            }
        }
        for (int i = 0; i < max_node; i++){
            if (!visited[i]){
                dfs1_for_kosaraju(i, adjacencyMatrix, visited, order);
            }
        }
        std::fill(visited.begin(), visited.end(), 0);
        int count = 1;
        for (int i = 0; i < max_node; i++){
            int v = order[max_node - i - 1];
            if (!visited[v]){
                std::cout << "Component " << count << ": ";
                dfs2_for_kosaraju(v, reverse, visited);
                std::cout << std::endl;
                count++;
            }
        }
        return distance;
    }
    void dfs1_for_kosaraju(int v, std::vector<std::vector<int>> &adjacencyMatrix, std::vector<int> &visited, std::vector<int> &order){
        Stack Stack;
        Stack.push(v);
        while (!Stack.is_empty()){
            v = Stack.front();
            Stack.pop();
            if (!visited[v]){
                visited[v] = 1;
                for (int i = 0; i < adjacencyMatrix.size(); i++){
                    if (adjacencyMatrix[v][i] != 0){
                        Stack.push(i);
                    }
                }
            }
            order.push_back(v);
        }
    }
    void dfs2_for_kosaraju(int v, std::vector<std::vector<int>> &adjacencyMatrix, std::vector<int> &visited){
        Stack Stack;
        Stack.push(v);
        while (!Stack.is_empty()){
            v = Stack.front();
            Stack.pop();
            if (!visited[v]){
                visited[v] = 1;
                std::cout << v + 1 << " ";
                for (int i = 0; i < adjacencyMatrix.size(); i++){
                    if (adjacencyMatrix[v][i] && !visited[i]){
                        Stack.push(i);
                    }
                }
            }
        }
    }

    std::vector<int> points_of_articulation(std::vector<std::vector<int>> &adjacencyMatrix,int max_node){
        std::vector<std::vector<int>> temparary_adjancy_matrix = adjacencyMatrix;
        std::vector<int> articulation_point;
        int count_component = conCompDFS(adjacencyMatrix);
        int buf_value=0;
        for(int i=0;i<max_node;i++){
            for(int j=0;j<temparary_adjancy_matrix.size();j++){
                temparary_adjancy_matrix[j].erase(temparary_adjancy_matrix[j].begin() + i);
                }
                temparary_adjancy_matrix.erase(temparary_adjancy_matrix.begin() + i);
                if(conCompDFS(temparary_adjancy_matrix)>count_component){
                    articulation_point.push_back((i+1));
                }
                temparary_adjancy_matrix = adjacencyMatrix;
        }
        return articulation_point;
    }

   struct Frame {
        Frame(int v, int p, int i) : v(v), p(p), i(i) {}
        int v;
        int p;
        int i;};
    void DFS_for_bridges(int n, const std::vector<std::vector<int>> &G) {
        std::vector<bool> used(n + 1, false);
        std::vector<int> ret(n + 1);  // the same as tup
        std::vector<int> enter(n + 1);  // the same as tin
        std::stack<Frame> s;
        s.push(Frame(1, -1, 0));
        int time = 1;
        while (!s.empty()) {
            Frame f = s.top();
            s.pop();
            int v = f.v;
            int p = f.p;
            int i = f.i;
            if (i == 0) {
                enter[v] = ret[v] = time++;
                used[v] = true;
            }
        // First part works befor DFS call
            if (i < G[v].size()) {
                int to = G[v][i];
                s.push(Frame(v, p, i + 1));
                if (to != p) {
                    if (used[to]) {
                        ret[v] = std::min(ret[v], enter[to]);
                    } 
                    else {
                        s.push(Frame(to, v, 0));
                    }
                }
            }
            //Generally here is virtual DFS recursive call, which we are simulate now
        // Second part after DFS call
            if (i > 0 && i <= G[v].size()) {
                int to = G[v][i - 1];
                if (to != p) {
                    ret[v] = std::min(ret[v], ret[to]);
                    if (ret[to] > enter[v]) {
                        std::cout << "bridge between: " << v << " and " << to<<std::endl;
                    
                    }
                }
            }
        }
    }
    
    
    //algorithm for finding a number of two-connected components
    int conCompDFS_for_two_connected_component(std::vector<std::vector<int>> &adjacencyMatrix){
        int max_node = adjacencyMatrix.size();
        std::vector<int> visited(max_node, 0);
        std::vector<int> order;
        for (int i = 0; i < max_node; i++){
            if (!visited[i]){
                dfs1_for_kosaraju1(i, adjacencyMatrix, visited, order);
            }
        }
        std::fill(visited.begin(), visited.end(), 0);
        int count = 1;
        for (int i = 0; i < max_node; i++){
            int v = order[max_node - i - 1];
            if (!visited[v]){
                dfs2_for_kosaraju2(v, adjacencyMatrix, visited);
                count++;
            }
        }
        return count;
    }
    void dfs1_for_kosaraju1(int v, std::vector<std::vector<int>> &adjacencyMatrix, std::vector<int> &visited, std::vector<int> &order){
        Stack Stack;
        Stack.push(v);
        while (!Stack.is_empty()){
            v = Stack.front();
            Stack.pop();
            if (!visited[v]){
                visited[v] = 1;
                for (int i = 0; i < adjacencyMatrix.size(); i++){
                    if (adjacencyMatrix[v][i] != 0){
                        Stack.push(i);
                    }
                }
            }
            order.push_back(v);
        }
    }
    void dfs2_for_kosaraju2(int v, std::vector<std::vector<int>> &adjacencyMatrix, std::vector<int> &visited){
        Stack Stack;
        Stack.push(v);
        while (!Stack.is_empty()){
            v = Stack.front();
            Stack.pop();
            if (!visited[v]){
                visited[v] = 1;
                std::cout << v + 1 << " ";
                for (int i = 0; i < adjacencyMatrix.size(); i++){
                    if (adjacencyMatrix[v][i] && !visited[i]){
                        Stack.push(i);
                    }
                }
            }
        }
    }


    void add_column_row(std::vector<std::vector<int>> &matrix, int size){
        for(int i=0;i<size;i++){
            matrix[i].push_back(0);
        }
        matrix.push_back(std::vector<int>(size+1, 0));
    }
    void delete_row_column(std::vector<std::vector<int>> &matrix, int size, int row, int column){
        for(int i=0;i<size;i++){
            matrix[i].erase(matrix[i].begin()+column);
        }
        matrix.erase(matrix.begin()+row);
    }
    int component_double_conected(std::vector<std::vector<int>> &matrix,std::vector<int> &articulation_points,int max_node){
        int size_articulation_points = articulation_points.size();
        std::vector<std::vector<int>> number_subgraphs_in_graph=matrix;
        int new_vertex = max_node-1;
        for(int k=0;k<size_articulation_points;k++){
                for(int j=0;j<matrix.size();j++){
                    if(number_subgraphs_in_graph[articulation_points[k]-1][j] == 1){
                        new_vertex++;
                        number_subgraphs_in_graph[articulation_points[k]-1][j] = 0;
                        number_subgraphs_in_graph[j][articulation_points[k]-1] = 0;
                        add_column_row(number_subgraphs_in_graph, new_vertex);
                        number_subgraphs_in_graph[new_vertex][j] = 1;
                        number_subgraphs_in_graph[j][new_vertex] = 1;
                        
                    }
                }
            }


        int del=1;
        for(int i=0;i<articulation_points.size();i++){
            delete_row_column(number_subgraphs_in_graph, number_subgraphs_in_graph.size(), articulation_points[i]-del, articulation_points[i]-del);
            del++;
        }
        

        int count_component = conCompDFS(number_subgraphs_in_graph);
        return count_component;
    }
    
};

    
    
    

    

    