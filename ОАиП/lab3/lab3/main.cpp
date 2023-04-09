#include <iostream>	
#include <conio.h>
using namespace std;
int summa(int a, int b) {
	cout << "Work function summa\n";
	return a + b;
}
int mult(int a, int b) {
	cout << "\nWork function multiplication";
	return a * b;
}
int fact(int a) {
	int f = 1;
	for (int i = 1; i < a + 1; i++) {
		f *= i;
	}
	cout << "\nWork function factorial";
	return f;
}

int main()
{
	int a, b, s, p;
	cout << "Enter the value of the variable  a=";
	cin >> a;
	cout << "Enter the value of the variable b=";
	cin >> b;
	s = summa(a, b);
	cout << "The sum of two numbers (a+b)= " << s;
	p = mult(a, b);
	cout << "\nThe multiplication of two numbers (a*b)= " << p;
	cout << "\nEnter the value of the variable f=";
	cin >> p;
	cout << "Factorial number  " << p << "   equal  " << fact(p) << endl;
	cout << endl;
	getchar();
	system("PAUSE");
	return 0;
}