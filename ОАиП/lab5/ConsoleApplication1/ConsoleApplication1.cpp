#include <iostream>
#include <string>
#include <windows.h>
using namespace std;

int main() {
	SetConsoleCP(1251); SetConsoleOutputCP(1251);
	int num_glas = 0, num_sogl = 0;
	char glasnie[] = "аеиоуюяыэё", soglasnie[] = "йцкнгшщзхъфвпрлджчсмтьб";
	string str;
	getline(cin, str);
	for (int i = 0; i < str.length(); i++) {
		for (int j = 0; j < sizeof(glasnie) / sizeof(char)-1; j++) {
			if (str[i] == glasnie[j]) num_glas++;
		}
		for (int j = 0; j < sizeof(soglasnie) / sizeof(char)-1; j++)
			if (str[i] == soglasnie[j]) num_sogl++;
	}
	if (num_glas > num_sogl) cout << "Гласных больше, чем согласных";
	else {
		if (num_glas < num_sogl) cout << "Согласных больше, чем гласных";
		else cout << "Согласных  столько же, сколько и гласных";
	}
}