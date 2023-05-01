#include <iostream>
#include <cmath>

using namespace std;

pair<int, int> fermat_factorization(int n) {
    int a = ceil(sqrt(n));
    int b2 = a*a - n;

    while (sqrt(b2) != floor(sqrt(b2))) {
        a++;
        b2 = a*a - n;
    }

    int x = sqrt(b2);
    int p = a + x;
    int q = a - x;

    return {p, q};
}

int main() {
    int n = 14789265460;

    auto [p, q] = fermat_factorization(n);
    cout << "Число " << n << " разложено на множители: " << p << " * " << q << endl;

    return 0;
}
