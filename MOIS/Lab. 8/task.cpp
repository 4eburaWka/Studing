#include <iostream>
#include <vector>
#include <fstream>
#include <sstream>
#include <time.h>
using namespace std;

struct Item{
    int weight, cost;
    Item(int weight, int cost){
        this->weight = weight; this->cost = cost;
    }
};

int knapsack(int W, vector<Item> &items){
    int max_cost = 0;
    int n = items.size();

    int current_weight, current_cost;
    for (int i = 0; i < (1 << n); i++){
        cout << i << endl;
        current_weight = current_cost = 0;
        for (int j = 0; j < n; j++){
            if (i & (1 << j)){
                current_weight += items[j].weight;
                current_cost += items[j].cost;
            }
        }
        if (current_weight == W and current_cost > max_cost)
            max_cost = current_cost;
    }
    return max_cost;
}

int main(){
    srand(time(NULL));
    
    string path; int W; 
    cout << "Введите путь к файлу: "; getline(cin, path); 
    cout << "Введите вес: "; cin >> W;
    ifstream file(path);
    string str; int weight, cost;
    vector<Item> items;
    while(getline(file, str)){ // считываем одну строку из файла
        istringstream iss(str); // создаем поток для чтения из строки
        iss >> weight >> cost;
        Item i(weight, cost);
        items.push_back(i);
    }
    file.close();

    struct timespec start, end;
    clock_gettime(CLOCK_REALTIME, &start);
    cout << knapsack(W, items) << endl;
    clock_gettime(CLOCK_REALTIME, &end);
    cout << "Время: " << (end.tv_sec - start.tv_sec) + (end.tv_nsec - start.tv_nsec) / 1000000000.0;
}
// C:\\Studing\\MOIS\\Lab. 8\\example_1