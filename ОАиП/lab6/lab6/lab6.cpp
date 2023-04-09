#include <iostream>
#include <math.h>
using namespace std;
int main() {
    int n,i=1;
    cin >> n;
    while ((pow(i,2)) < n) {
        i++;
    }
    cout << pow(i, 2);
}