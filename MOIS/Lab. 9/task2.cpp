#include <iostream>
#include <fstream>
#include "../get_time.h"
using namespace std;

int main(){
    ifstream file("E:\\Studing\\MOIS\\Lab. 9\\task2");
    long long n, a, b, c;
    long long div_a = 0, div_b = 0, div_c = 0;
    file >> n >> a >> b >> c;
    start_clock();
    for (unsigned i = 0; i < n; i++){
        if (i % a == 0)
            div_a++;
        if(i % b == 0)
            div_b++;
        if(i % c == 0)
            div_c++;
    }
    stop_clock();
    cout << "Делятся на " << a << ": " << div_a << endl;
    cout << "Делятся на " << b << ": " << div_b << endl;
    cout << "Делятся на " << c << ": " << div_c << endl;
}