#include <iostream>
#include <vector>
#include <fstream>
#include <sstream>
#include <time.h>
#include <algorithm>
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

bool cpm(Item a, Item b){
    float one = (a.cost / (float)a.weight), two = (b.cost / (float)b.weight);
    return one < two;
}

void knapsack(int W, vector<Item> &items, vector<int> &subs, vector<int> &costs){
    int n = items.size(), cur_w;
    while (1){
        cur_w = get_weight(items, subs);
        if (cur_w < W){
            subs.push_back(n-1);
        } 
        else if (cur_w == W)
            break;
        else if (cur_w > W){
            while (subs.back() == 0 and subs.size() != 0)
                subs.pop_back();
            if (subs.size() == 0)
                break;
            else subs.back() -= 1;
        }
    }
    for (int el: subs)
        cout << items[el].weight << " ";
    cout << endl << get_cost(items, subs) << endl;
}

int main(){
    string path="/home/kali/Studing/MOIS/Lab. 8/example_2"; int W=998, n=0; 
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
    sort(items.begin(), items.end(), cpm);
    clock_gettime(CLOCK_REALTIME, &start);
    knapsack(W, items, subs, costs); // оооочень медленная функция когда-то была, но уже все ок)))
    clock_gettime(CLOCK_REALTIME, &end);
    cout << "Время: " << (end.tv_sec - start.tv_sec) + (end.tv_nsec - start.tv_nsec) / 1000000000.0 << endl;
}