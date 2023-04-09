#include <math.h>
#include <iostream>
using namespace std;

int main() {
	setlocale(LC_CTYPE, "Russian");

	float a, b{}, c{};
	cin >> a >> b >> c;

	if (pow(a, 2) + pow(b, 2) == pow(c, 2) || pow(a, 2) + pow(c, 2) == pow(b, 2) || pow(c, 2) + pow(b, 2) == pow(a, 2)) {
		cout << "Прямоугольный, ";
	}
	else {
		if (pow(a, 2) + pow(b, 2) <= pow(c, 2) || pow(a, 2) + pow(c, 2) <= pow(b, 2) || pow(c, 2) + pow(b, 2) <= pow(a, 2)) {
			cout << "Остроугольный, ";
		}
		else cout << "Тупоугольный, ";
	}

	if (a == b && b == c) cout << "равностронний.";
	else {
		if (a == b || a == c || b == c) cout << "равнобедренный.";
		else cout << "разносторонний.";
	}
}