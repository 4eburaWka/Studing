#include <fstream>
#include <iostream>
#include <vector>
using namespace std;

int getEdgesCount(string path){
	//возвращает количество ребер в графе 
    ifstream file(path);
    string numbers;
    file >> numbers;
    return (numbers.find('[') + 2) / 6;
}

int getTopsCount(string path){
	//возвращает количество вершин в графе 
    ifstream file(path);
    char numbers[100];
    file >> numbers; 
    int connections[100][2], weights[100]; 
    

    char temp[] = "00";
    int i = 0, t = 1, n = 0, m = 0;
    while (true){
        while (numbers[++i] != ',')
            temp[t--] = numbers[i];
        connections[n][m++] = (temp[0] - 48) * 10 + temp[1] - 48;
        temp[0] = '0';
        t = 1;
        while (numbers[++i] != '}')
            temp[t--] = numbers[i];
        connections[n++][m--] = (temp[0] - 48) * 10 + temp[1] - 48;
        temp[0] = '0';
        i += 2;
        t = 1;
        if (numbers[i-1] == '[')
            break;
    }
    int max = 0;
    for (int i = 0; i < getEdgesCount(path); i++){
        if (max < connections[i][0])
            max = connections[i][0];
        else if (max < connections[i][1])
            max = connections[i][1];
    }
    return max;
}

int** edgesConnections(string path){
    ifstream file(path);
    char numbers[100];
    file >> numbers;
    int connections[100][2]; 

    const int tops = getTopsCount(path), edges = getEdgesCount(path);
    char temp[] = "00";
    int i = 0, t = 1, n = 0, m = 0;
    while (true){
        while (numbers[++i] != ',')
            temp[t--] = numbers[i];
        connections[n][m++] = (temp[0] - 48) * 10 + temp[1] - 48;
        temp[0] = '0';
        t = 1;
        while (numbers[++i] != '}')
            temp[t--] = numbers[i];
        connections[n++][m--] = (temp[0] - 48) * 10 + temp[1] - 48;
        temp[0] = '0';
        i += 2;
        t = 1;
        if (numbers[i-1] == '[')
            break;
    }

    int **edgesCons; 
    edgesCons = new int*[edges];
    for (int i = 0; i < edges; i++)
        edgesCons[i] = new int[2];
    for (int i = 0; i < edges; i++){
        edgesCons[i][0] = connections[i][0];
        edgesCons[i][1] = connections[i][1];
    }
    return edgesCons;
}

int** adjacencyMatrixFromConnections(string path){
	// возвращает матрицу смежности из списка связей с заданными весами (сначала сввязи, потом веса) ДЛЯ ОРГРАФА
	// {1,2},{1,3},{2,3}[
    ifstream file(path);
    char numbers[100];
    file >> numbers; 
    int connections[100][2]; 
    

    const int tops = getTopsCount(path);
    char temp[] = "00";
    int i = 0, t = 1, n = 0, m = 0;
    while (true){
        while (numbers[++i] != ',')
            temp[t--] = numbers[i];
        connections[n][m++] = (temp[0] - 48) * 10 + temp[1] - 48;
        temp[0] = '0';
        t = 1;
        while (numbers[++i] != '}')
            temp[t--] = numbers[i];
        connections[n++][m--] = (temp[0] - 48) * 10 + temp[1] - 48;
        temp[0] = '0';
        i += 2;
        t = 1;
        if (numbers[i-1] == '[')
            break;
    }
    const int edges = getEdgesCount(path);
    int **adjacencyMatrix; 
    adjacencyMatrix = new int*[tops];
    for (int i = 0; i < tops; i++)
        adjacencyMatrix[i] = new int[tops];
     
    for (int i = 0; i < tops; i++){ 
        for (int j = 0; j < tops; j++) 
            adjacencyMatrix[i][j] = 0; 
    } 
    n = 0;
    for (int i = 0; i < edges; i++){ 
        adjacencyMatrix[connections[i][0] - 1][connections[i][1] - 1] = 1;
        adjacencyMatrix[connections[i][1] - 1][connections[i][0] - 1] = 1;
    }
    return adjacencyMatrix;
}

int** adjacencyMatrixFromConnectionsWithHeights(string path){
	// возвращает матрицу смежности из списка связей с заданными весами (сначала сввязи, потом веса)
	// {1,2},{1,3},{2,3}[1,2,3]
    ifstream file(path);
    char numbers[100];
    file >> numbers; 
    int connections[100][2], weights[100]; 
    

    const int tops = getTopsCount(path);
    char temp[] = "00";
    int i = 0, t = 1, n = 0, m = 0;
    while (true){
        while (numbers[++i] != ',')
            temp[t--] = numbers[i];
        connections[n][m++] = (temp[0] - 48) * 10 + temp[1] - 48;
        temp[0] = '0';
        t = 1;
        while (numbers[++i] != '}')
            temp[t--] = numbers[i];
        connections[n++][m--] = (temp[0] - 48) * 10 + temp[1] - 48;
        temp[0] = '0';
        i += 2;
        t = 1;
        if (numbers[i-1] == '[')
            break;
    }
    const int edges = getEdgesCount(path);

    n = 0;
    while (i < 200){
        while (numbers[i] != ',' && numbers[i] != ']')
            temp[t--] = numbers[i++];
        weights[n++] = (temp[0] - 48) * 10 + temp[1] - 48;
        temp[0] = '0';
        t = 1; 
        if (numbers[i] == ']')
            break;
        i++;
    }
    int **adjacencyMatrix; 
    adjacencyMatrix = new int*[tops];
    for (int i = 0; i < tops; i++)
        adjacencyMatrix[i] = new int[tops];
     
    for (int i = 0; i < tops; i++){ 
        for (int j = 0; j < tops; j++) 
            adjacencyMatrix[i][j] = 0; 
    } 
    n = 0;
    for (int i = 0; i < edges; i++){ 
        adjacencyMatrix[connections[i][0] - 1][connections[i][1] - 1] = weights[n]; 
        adjacencyMatrix[connections[i][1] - 1][connections[i][0] - 1] = weights[n++]; 
    }
    return adjacencyMatrix;
}

int** adjacencyMatrixFromConnectionsWithHeightsORGRAPH(string path){
	// возвращает матрицу смежности из списка связей с заданными весами (сначала сввязи, потом веса) ДЛЯ ОРГРАФА
	// {1,2},{1,3},{2,3},{2,1},{3,1},{3,2}[1,2,3,1,2,3]
    ifstream file(path);
    char numbers[100];
    file >> numbers; 
    int connections[100][2], weights[100]; 
    

    const int tops = getTopsCount(path);
    char temp[] = "00";
    int i = 0, t = 1, n = 0, m = 0;
    while (true){
        while (numbers[++i] != ',')
            temp[t--] = numbers[i];
        connections[n][m++] = (temp[0] - 48) * 10 + temp[1] - 48;
        temp[0] = '0';
        t = 1;
        while (numbers[++i] != '}')
            temp[t--] = numbers[i];
        connections[n++][m--] = (temp[0] - 48) * 10 + temp[1] - 48;
        temp[0] = '0';
        i += 2;
        t = 1;
        if (numbers[i-1] == '[')
            break;
    }
    const int edges = getEdgesCount(path);

    n = 0;
    while (i < 200){
        while (numbers[i] != ',' && numbers[i] != ']')
            temp[t--] = numbers[i++];
        weights[n++] = (temp[0] - 48) * 10 + temp[1] - 48;
        temp[0] = '0';
        t = 1; 
        if (numbers[i] == ']')
            break;
        i++;
    }
    int **adjacencyMatrix; 
    adjacencyMatrix = new int*[tops];
    for (int i = 0; i < tops; i++)
        adjacencyMatrix[i] = new int[tops];
     
    for (int i = 0; i < tops; i++){ 
        for (int j = 0; j < tops; j++) 
            adjacencyMatrix[i][j] = 0; 
    } 
    n = 0;
    for (int i = 0; i < edges; i++){ 
        adjacencyMatrix[connections[i][0] - 1][connections[i][1] - 1] = weights[n++]; 
    }
    return adjacencyMatrix;
}

int** adjacencyMatrixFromConnectionsORGRAPH(string path){
	// возвращает матрицу смежности из списка связей с заданными весами (сначала сввязи, потом веса) ДЛЯ ОРГРАФА
	// {1,2},{1,3},{2,3},{2,1},{3,1},{3,2}
    ifstream file(path);
    char numbers[100];
    file >> numbers; 
    int connections[100][2]; 
    

    const int tops = getTopsCount(path);
    char temp[] = "00";
    int i = 0, t = 1, n = 0, m = 0;
    while (true){
        while (numbers[++i] != ',')
            temp[t--] = numbers[i];
        connections[n][m++] = (temp[0] - 48) * 10 + temp[1] - 48;
        temp[0] = '0';
        t = 1;
        while (numbers[++i] != '}')
            temp[t--] = numbers[i];
        connections[n++][m--] = (temp[0] - 48) * 10 + temp[1] - 48;
        temp[0] = '0';
        i += 2;
        t = 1;
        if (numbers[i-1] == '[')
            break;
    }
    const int edges = getEdgesCount(path);

    int **adjacencyMatrix; 
    adjacencyMatrix = new int*[tops];
    for (int i = 0; i < tops; i++)
        adjacencyMatrix[i] = new int[tops];
     
    for (int i = 0; i < tops; i++){ 
        for (int j = 0; j < tops; j++) 
            adjacencyMatrix[i][j] = 0; 
    } 
    n = 0; i = 0;
    for (int i = 0; i < edges; i++){ 
        adjacencyMatrix[connections[i][0] - 1][connections[i][1] - 1] = 1;
    }
    return adjacencyMatrix;
}



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
class queue
{
private:
    vector<int> array;
    int tail = 0; 
public:
    // Pushes an element to the end of the queue
    void push(int x) 
    {
        array.push_back(x);
        tail++;
    }

    // Removes the first element of the queue
    void pop() 
    {
        array.erase(array.cbegin());
        tail--;
    }

    // Returns the first element of the queue
    int front()
    {
        return array[0];
    }

    // Returns true if the queue is empty
    bool is_empty() 
    {
        return tail == 0;
    }

    // Prints the queue
    void print()
    {
        int l = array.size();
        for (int i = 0; i < l; i++)
        {
            std::cout << array[i];
        }
        std::cout << std::endl;
    }

    // swap two elements in the queue
    void swap(int i, int j)
    {
        int temp = array[i];
        array[i] = array[j];
        array[j] = temp;
    }

    // [] operator overloading
    int operator[](int i)
    {
        return array[i];
    }
};
class list{
    public:
        int list[100];
        int length = 0;
        void append(int num){
            list[length++] = num;
        }
        int last(){
            return list[length-1];
        }
        int find(int el){
            for (int i = 0; i < length; i++){
                if (list[i] == el)
                    return i;
            }
            return -1;
        }
};
