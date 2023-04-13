#include <iostream>
#include <cmath>
using namespace std;

long long gcd(long long a, long long b) {
    if (b == 0) return a;
    return gcd(b, a % b);
}

pair<long long, long long> fermat_factorization(long long n) {
    long long a, x, y;
    while (true) {
        a = rand() % (n - 1) + 1;
        x = a * a - n;
        y = sqrt(x);
        if (y * y == x) {
            long long p = gcd(n, a - y);
            long long q = gcd(n, a + y);
            if (p != 1 && q != 1) {
                return make_pair(p, q);
            }
        }
    }
}

int main() {
    long long n = 400;
    pair<long long, long long> factors = fermat_factorization(n);
    cout << "The factors of " << n << " are " << factors.first << " and " << factors.second << endl;
    return 0;
}
