#include <iostream>
#include <cmath>
using namespace std;

bool is_prime(unsigned long long n) {
    if (n < 2) {
        return false;
    }
    for (unsigned long long i = 2; i <= sqrt(n); i++) {
        if (n % i == 0) {
            return false;
        }
    }
    return true;
}

unsigned long long generate_prime(unsigned long long k) {
    unsigned long long n = pow(2, k) - 1;
    unsigned long long i = 2;
    while (!is_prime(n)) {
        n = pow(2, k) - 1;
        n = n * i;
        i++;
    }
    return n;
}

unsigned long long main() {
    unsigned long long k;
    cout << "Enter k: ";
    cin >> k;
    unsigned long long prime = generate_prime(k);
    cout << "Prime number: " << prime << endl;
 }
