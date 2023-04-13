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

    int check_arr[] = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
        47, 53, 59, 67, 71, 83, 89, 101, 107, 109, 113, 127, 131, 137,
        139, 149, 157, 167, 179, 181, 191, 197, 199, 211};
    
    for (int num: check_arr)
        if (prime % (float)num == 0) {
            cout << "Число " << prime << "делится на " << num << endl;
            return 0;
    }
}