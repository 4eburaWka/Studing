#include <math.h>
#include <iostream>
using namespace std;

int main() {
	setlocale(LC_CTYPE, "Russian");

	float a, b{}, c{};
	cin >> a >> b >> c;

	if (pow(a, 2) + pow(b, 2) == pow(c, 2) || pow(a, 2) + pow(c, 2) == pow(b, 2) || pow(c, 2) + pow(b, 2) == pow(a, 2)) {
		cout << "�������������, ";
	}
	else {
		if (pow(a, 2) + pow(b, 2) <= pow(c, 2) || pow(a, 2) + pow(c, 2) <= pow(b, 2) || pow(c, 2) + pow(b, 2) <= pow(a, 2)) {
			cout << "�������������, ";
		}
		else cout << "������������, ";
	}

	if (a == b && b == c) cout << "�������������.";
	else {
		if (a == b || a == c || b == c) cout << "��������������.";
		else cout << "��������������.";
	}
}