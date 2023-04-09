#include <stdio.h>  

int main() { 
    FILE *file;
    char numbers[100]; 
    const int tops = 8, edges = 8; // -кол-во вершин и ребер
    int connections[edges][2]; 
    
    file = fopen("connection.txt", "r");
    fgets(numbers, 256, file);  
    
    
    char temp[] = "00";
    int i = 0, t = 1, n = 0, m = 0;
    while (i < 47){
        while (numbers[++i] != ',')
            temp[t--] = numbers[i];
        connections[n][m++] = (temp[0] - 48) * 10 + temp[1] - 48;
        temp[0] = '0';
        t = 1;
        while (numbers[++i] != ')')
            temp[t--] = numbers[i];
        connections[n++][m--] = (temp[0] - 48) * 10 + temp[1] - 48;
        temp[0] = '0';
        i += 2;
        t = 1;

    }
    

    // Матрица смежности
    int adjacencyMatrix[tops][tops]; 
     
    for (int i = 0; i < tops; i++){ 
        for (int j = 0; j < tops; j++) 
            adjacencyMatrix[i][j] = 0; 
    } 
     
    for (int i = 0; i < tops; i++){ 
        adjacencyMatrix[connections[i][0] - 1][connections[i][1] - 1] = 1; 
        adjacencyMatrix[connections[i][1] - 1][connections[i][0] - 1] = 1; 
    } 
     
    printf("{");
    for (int i = 0; i < tops; i++){ 
        printf("{");
        for (int j = 0; j < tops; j++) 
            printf("%d, ", adjacencyMatrix[i][j]); 
        printf("\b\b},\n");
    } 
    printf("}\n\n"); 

    // Матрица инцидентности 
    int incidenceMatrix[tops][edges]; 

    for (int i = 0; i < tops; i++){ 
        for(int j = 0; j < edges; j++) 
            incidenceMatrix[i][j] = 0; 
    } 

    for (int i = 0; i < edges; i++){ 
        incidenceMatrix[connections[i][0] - 1][i] = 1; 
        incidenceMatrix[connections[i][1] - 1][i] = 1; 
    } 
    printf("{");
    for (int i = 0; i < tops; i++){ 
        printf("{");
        for(int j = 0; j < edges; j++) 
            printf("%d, ", incidenceMatrix[i][j]); 
        printf("\b\b},\n");  
    }  
    printf("}\n");
    return 0; 
}