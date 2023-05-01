#include <iostream>
#include <cstdlib> // Для функций rand и srand
#include <ctime> // Для функции time
using namespace std;
int gcd(int a, int b);
int pow_modulo(int a, int b, int n);
bool lehmann_test(int n, int k) {
// Если n меньше двух, то оно не простое
if (n < 2) {
return false;
}

// Если n равно 2, то оно простое
if (n == 2) {
    return true;
}

// Если n четное, то оно не простое
if (n % 2 == 0) {
    return false;
}

// Устанавливаем начальное значение генератора случайных чисел
srand(time(NULL));

// Выбираем k случайных чисел a из интервала [2, n-1]
for (int i = 0; i < k; i++) {
    int a = rand() % (n-2) + 2;
    
    // Если НОД(a, n) не равен 1, то n не простое
    if (gcd(a, n) != 1) {
        return false;
    }
    
    // Если a^(n-1) не равно 1 по модулю n, то n не простое
    if (pow_modulo(a, n-1, n) != 1) {
        return false;
    }
}

// Если все k проверок пройдены успешно, то n вероятно простое
return true;

}

int gcd(int a, int b) {
// Находим наибольший общий делитель двух чисел a и b
while (b) {
int t = b;
b = a % b;
a = t;
}
return a;
}

int pow_modulo(int a, int b, int n) {
// Возвращает a^b mod n
int result = 1;
while (b) {
if (b & 1) {
result = (result * a) % n;
}
a = (a * a) % n;
b >>= 1;
}
return result;
}

int main() {
int n = 238988988; // Проверяемое число
int k = 10; // Количество итераций

bool is_prime = lehmann_test(n, k);
if (is_prime) {
    cout << n << " is probably prime" << std::endl;
} else {
    cout << n << " is composite" << std::endl;
}

return 0;

}