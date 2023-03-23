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

template <typename T>
int find_max(vector<T> costs){
    if (costs.size() == 0)
        return -1;
    int sum = 0, index;
    for (int i = 0; i < costs.size(); i++){
        if(costs[i] > sum){
            sum = costs[i];
            index = i;
        }
    }
    return index;
}

template <typename T>
bool is_full_of(vector<T> &vec, int el){
    for (int i: vec)
        if (i != el)
            return false; 
    return true;
}

void knapsack(int W, vector<Item> &items, vector<int> &subs, vector<int> &costs){
    int n = items.size(), cur_w;
    while (1){
        cur_w = get_weight(items, subs);
        if (cur_w < W){
            subs.push_back(n-1);
        } 
        else if (cur_w == W){
            costs.push_back(get_cost(items, subs)); cout << costs.back() << endl;
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

void knapsack2(int W, vector<Item> &items){
    vector<int> item_weights, item_costs, subs; vector<float> costs, costs2;
    for (Item item: items){
        item_weights.push_back(item.weight);
        item_costs.push_back(item.cost);
    }
    for (int i = 0; i < item_weights.size(); i++){
        costs.push_back(item_costs[i] / (float)item_weights[i]);
    }
    costs2 = costs;
    int most_profitable_index = find_max(costs); // находим индекс самого выгодного продукта
    int cur_w, iter = items.size();
    while (cur_w < W){
        subs.push_back(most_profitable_index);
        cur_w = get_weight(items, subs);
    }
    if (cur_w == W){
        cout << get_cost(items, subs) << endl;
        return;
    }
    while (iter--){
        while (is_full_of(costs, 0)){
            subs.pop_back();
            cur_w = get_weight(items, subs);
            costs[most_profitable_index] = 0;
            most_profitable_index = find_max(costs);
            while (cur_w < W){
                subs.push_back(most_profitable_index);
                cur_w = get_weight(items, subs);
            }
            if (cur_w == W){
                cout << get_cost(items, subs) << endl;
                return;
            }
        }
        costs = costs2;
        while (cur_w > W - )
        subs.pop_back();
    }
    cout << "Комбинация не найдена" << endl;
}

int main(){
    srand(time(NULL));
    
    string path="/home/kali/Studing/MOIS/Lab. 8/example_1"; int W=998, n=0; 
    // cout << "Введите путь к файлу: "; getline(cin, path); 
    cout << "Введите вес: "; cin >> W;
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
    // knapsack(W, items, subs, costs); // оооочень медленная функция
    knapsack2(W, items);
    clock_gettime(CLOCK_REALTIME, &end);
    cout << "Время: " << (end.tv_sec - start.tv_sec) + (end.tv_nsec - start.tv_nsec) / 1000000000.0 << endl;
}