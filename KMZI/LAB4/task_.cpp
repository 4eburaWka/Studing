#include <iostream>
#include "../Libs/bignumber.h"
using namespace pr0crustes;
using namespace std;

bool isPrime(BigNumber N);
void dividing(BigNumber N);
bool fermat_factorization(BigNumber n);
void combined_method(BigNumber n);
BigNumber sqrt(BigNumber n);

int main() {
    short menu;
    BigNumber N;
    while (true){
        cout << "1. Метод пробного деления.\n" << 
        "2. Метод Ферма (без операции деления).\n" << 
        "3. Комбинированный метод.\n" <<
        "4. Выход из программы.\n> ";
        cin >> menu;

        switch(menu){
        case 1:
            cout << "Введите число: "; cin >> N;
            dividing(N); cout << endl << endl;
            break;
        case 2:
            cout << "Введите число: "; cin >> N;
            fermat_factorization(N); cout << endl;
            break;
        case 3:
            cout << "Введите число: "; cin >> N;
            combined_method(N); cout << endl;
            break;
        case 4:
            return 0;
            break;
        }
    }
}
BigNumber sqrt(BigNumber n) { 
    BigNumber x = n; 
    BigNumber y = (x + n / x) / 2; 
    while (y < x) { 
        x = y; 
        y = (x + n / x) / 2; 
    } 
    return x; 
} 

bool isPrime(BigNumber n){
    bool is_prime = true;
    for (BigNumber i = 2; i <= sqrt(n); i += 2) {
        if (n % i == 0) {
            is_prime = false;
            break;
        }
    }
    return is_prime;
}

void dividing(BigNumber n){
    if (n % 2 == 0) {
        cout << "2 ";
        n /= 2;
    }

    for (BigNumber i = 3; i <= sqrt(n); i += 2) {
        while (n % i == 0) {
            cout << i << " ";
            n /= i;
        }
    }

    if (n > 2) {
        cout << n;
    }
}


bool fermat_factorization(BigNumber n) {
    BigNumber a = sqrt(n); // находим первое число, ближайшее к sqrt(n)
    BigNumber b2 = a*a - n; // b^2 = a^2 - n
    BigNumber b = sqrt(b2);
    unsigned count = 0; // ограничение на количество итераций

    while (b * b != b2) { // если b не целое, то увеличиваем a и пересчитываем b^2
        a++;
        b2 = a*a - n;
        b = sqrt(b2);
        count++;
        if (count > 100) { // ограничение на количество итераций
            return false;
        }
    }

    cout << a - b << " " << a + b << endl;
    return true;
}

void combined_method(BigNumber n){
    bool is_prime = isPrime(n);

    if (is_prime) {
        cout << n << " is a prime number." << endl;
        return;
    }

    dividing(n);

    cout << "\n\nМетод Ферма: " << endl;
    BigNumber k = sqrt(n);
    while (true) {
        BigNumber r = sqrt(k * k - n);
        if (r * r == k * k - n) {
            cout << (k - r) << (k + r) << endl;
            return;
        }
        k++;
    }
}
