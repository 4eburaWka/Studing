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

int get_weight(vector<Item> &items, vector<int> &subs){
    int sum = 0;
    int len = subs.size();
    for (int i = 0; i < len; i++)
        sum += items[subs[i]].weight;
    return sum;
}

int get_cost(vector<Item> &items, vector<int> &subs){
    int sum = 0;
    for (int i = 0; i < subs.size(); i++)
        sum += items[subs[i]].cost;
    return sum;
}

int find_max(vector<int> costs){
    if (costs.size() == 0)
        return 0;
    int sum = 0;
    for (int i = 0; i < costs.size(); i++){
        if(costs[i] > sum)
            sum = costs[i];
    }
    return sum;
}

void knapsack(int W, vector<Item> &items, vector<int> &subs, vector<int> &costs){
    int n = items.size(), cur_w;
    while (1){
        cur_w = get_weight(items, subs);
        if (cur_w < W){
            subs.push_back(n-1);
        } 
        else if (cur_w == W){
            costs.push_back(get_cost(items, subs));
            while (subs.back() == 0 and subs.size() != 0)
                subs.pop_back();
            if (subs.size() == 0)
                break;
            else subs.back() -= 1;
        } 
        else if (cur_w > W){
            while (subs.back() == 0 and subs.size() != 0)
                subs.pop_back();
            if (subs.size() == 0)
                break;
            else subs.back() -= 1;
        }
    }
    cout << find_max(costs) << endl;
}

int main(){
    srand(time(NULL));
    
    string path="E:\\Studing\\MOIS\\Lab. 8\\example_1"; int W=1000, n=0; 
    // cout << "Введите путь к файлу: "; getline(cin, path); 
    // cout << "Введите вес: "; cin >> W;
    ifstream file(path);
    string str; int weight, cost;
    vector<Item> items;
    while(getline(file, str)){ // считываем одну строку из файла
        istringstream iss(str); // создаем поток для чтения из строки
        iss >> weight >> cost;
        Item i(weight, cost);
        items.push_back(i);
        n++;
    }
    file.close();

    vector<int> subs = {n-1}, costs;
    struct timespec start, end;
    clock_gettime(CLOCK_REALTIME, &start);
    knapsack(W, items, subs, costs);
    // cout << ans << endl;
    clock_gettime(CLOCK_REALTIME, &end);
    cout << "Время: " << (end.tv_sec - start.tv_sec) + (end.tv_nsec - start.tv_nsec) / 1000000000.0;
}
// C:\\Studing\\MOIS\\Lab. 8\\example_1