#include <iostream>
#include <cmath>
using namespace std;

bool is_prime(int n) {
    if (n < 2) {
        return false;
    }
    for (int i = 2; i <= sqrt(n); i++) {
        if (n % i == 0) {
            return false;
        }
    }
    return true;
}

int generate_prime(int k) {
    int n = pow(2, k) - 1;
    int i = 2;
    while (!is_prime(n)) {
        n = pow(2, k) - 1;
        n = n * i;
        i++;
    }
    return n;
}

int main() {
    int k;
    cout << "Enter k: ";
    cin >> k;
    int prime = generate_prime(k);
    cout << "Prime number: " << prime << endl;
 }
