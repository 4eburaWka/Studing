#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

const int N = 10000;

int main() {
    int p = 113; // большое простое число
    int a = 237; // число, взаимно простое с p
    unsigned long long int seed = 123563514615412348; // начальное значение
    int x = seed;

    // генерируем перестановку для обращения
    vector<int> perm(N);
    for (int i = 0; i < N; i++) {
        perm[i] = i;
    }
    random_shuffle(perm.begin(), perm.end());
    // генерируем последовательность                
    vector<int> seq(N);
    for (int i = 0; i < N; i++) {

        x = abs((a * x) % p);
        seq[i] = x;
    }

    // обращаем последовательность
    vector<int> inv_seq(N);
    for (int i = 0; i < N; i++) {
        inv_seq[perm[i]] = seq[i];
    }

    // выводим результаты
    cout << "Исходная последовательность: ";
    for (int i = 0; i < N; i++) {
        cout << seq[i] << " ";
    }
    cout << endl;

    cout << "Обращенная последовательность: ";
    for (int i = 0; i < N; i++) {
        cout << inv_seq[i] << " ";
    }
    cout << endl;

  // вычисляем период последовательности
    int period = 1;
    for (int i = 1; i < N; i++) {
        if (inv_seq[i] != inv_seq[0]) {
            period = i;
            break;
        }
    }
    cout << "Период последовательности: " << period << endl;

    return 0;
}