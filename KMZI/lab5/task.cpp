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
        // n = pow(2, k) - 1;
        // n = n * i;
        // i++;
        n *= 2;
        n++;
    }
    return n;
}

int main() {
    unsigned long long k;
    cout << "Enter k: ";
    cin >> k;
    unsigned long long prime = generate_prime(k);
    cout << "Prime number: " << prime << endl;

    int check_arr[] = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
        47, 53, 59, 67, 71, 83, 89, 101, 107, 109, 113, 127, 131, 137,
        139, 149, 157, 167, 179, 181, 191, 197, 199, 211};
    
    for (int num: check_arr)
        if (prime % num == 0) {
            cout << "Число " << prime << " делится на " << num << endl;
            return 0;
    }
 }
