#include <stdio.h>
#include <conio.h>

int summa(int a, int b) {
	printf("Work function summa\n");
	return a + b;
}

int mult(int a, int b) {
	printf("\nWork function multiplication");
	return a * b;
}

int fact(int a) {
	int f = 1;
	for (int i = 1; i < a + 1; i++) {

		f *= i;
	}
	printf("\nWork function factorial");
	return f;
}

int main()
{
	int a, b, s, p;
	printf("Enter the value of the variable  a=");
	scanf_s("%d", &a);
	printf("\nEnter the value of the variable b=");
	scanf_s("%d", &b);
	s = summa(a, b);
	printf("The sum of two numbers (a+b)=%d", s);
	p = mult(a, b);
	printf("\nThe multiplication of two numbers (a*b)=%d", p);
	printf("\nEnter the value of the variable f=");
	scanf_s("%d", &p);
	printf("\nFactorial number %d equal %d", p, fact(p));
	getchar();
	scanf_s("Vvod s=", &s);
	return 0;
}