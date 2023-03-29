#include <iostream>
#include "./CongruentGen.h"
using namespace std;

int main() {
    cout << "B = {{3, 0}, {3, 1}, {3, 2}}, n = 15:\n";
    vector<vector<unsigned long long>> args1 = {{3, 0}, {3, 1}, {3, 2}};
    CongruentGen generator1(args1, 15);
    for (int i = 0; i < 20; i++) {
        cout << generator1.gen() << " ";
    }
    cout << "\n===========================================================\n";

    cout << "{{25, 17}, {13, 11}, {17, 19}, {23, 7}, {29, 13}}, n = 15:\n";
    vector<vector<unsigned long long>> args2 = {{25, 17}, {13, 11}, {17, 19}, {23, 7}, {29, 13}};
    CongruentGen generator2(args2, 15);
    for (int i = 0; i < 30; i++) {
        cout << generator2.gen() << " ";
    }
}
