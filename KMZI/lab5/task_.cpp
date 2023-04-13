#include <iostream>
#include "../Libs/bignumber.h"
using namespace std;
using namespace pr0crustes;

BigNumber sqrt(BigNumber n) {
    BigNumber x = n; 
    BigNumber y = (x + n / x) / 2; 
    while (y < x) { 
        x = y; 
        y = (x + n / x) / 2; 
    } 
    return x; 
}

bool is_prime(BigNumber n) {
    if (n < 2) {
        return false;
    }
    for (BigNumber i = 2; i <= sqrt(n); i++) {
        if (n % i == 0) {
            return false;
        }
    }
    return true;
}

BigNumber generate_prime(BigNumber k) {
    BigNumber n = BigNumber(2).pow(k) - 1;
    BigNumber i = 2;
    while (!is_prime(n)) {
        n = BigNumber(2).pow(k) - 1;
        n = n * i;
        i++;
    }
    return n;
}

int main() {
    BigNumber k;
    cout << "Enter k: ";
    cin >> k;
    BigNumber prime = generate_prime(k);
    cout << "Prime number: " << prime << endl;
}