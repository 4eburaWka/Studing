#include <iostream>
#include "../get_time.h"
using namespace std;

bool NextSet(int *a, int n){
    int j = n - 2;
    while (j != -1 && a[j] >= a[j + 1]) 
        j--;
    if (j == -1)
        return false; // больше перестановок нет
    int k = n - 1;
    while (a[j] >= a[k]) 
        k--;
    swap(a[j], a[k]);
    int l = j + 1, r = n - 1; // сортируем оставшуюся часть последовательности
    while (l < r)
        swap(a[l++], a[r--]);
    return true;
}

int main(){
    unsigned short N; unsigned iter = 0;
    cout << "Введите N: "; cin >> N;

    int arr[N];
    for (short i = 0; i < N; i++){
        arr[i] = i + 1;
    }
    start_clock();
    do{
        for (int x = 0; x < N; x++)
            if(arr[x] == x + 1){
                cout << ++iter << ": ";
                for (int z = 0; z < N; z++)
                    cout << arr[z];
                cout << endl;
            }
    } while (NextSet(arr, N));
    stop_clock();
}