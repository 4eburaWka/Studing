#include <iostream>
#include <windows.h>
using namespace std;

bool key[4];

short getkey() {
	int i = 37;

	while (i < 42)
		key[i - 38] = GetAsyncKeyState(i++) != 0 ? 1 : 0;
	if (key[0] != 0 && key[1] == 0 && key[2] == 0 && key[3] == 0)
		return 3;
	else {
		if (key[0] == 0 && key[1] != 0 && key[2] == 0 && key[3] == 0)
			return 4;
		else {
			if (key[0] == 0 && key[1] == 0 && key[2] != 0 && key[3] == 0)
				return 1;
			else {
				if (key[0] == 0 && key[1] == 0 && key[2] == 0 && key[3] != 0)
					return 2;
				else
					return 0;
			}
		}
	}
}

int main() {
	//setlocale(LC_ALL, "rus");
	bool stop = 1;
	char field[25][25];
	char str[20], str1[20];
	gets_s(str1);
	const int buff = sizeof(str1) / sizeof(str1[0]);
	// реверс массива
	for (int x = 0; x < buff; x++)
		str[x] = str1[19 - x];

	int xr[buff], yr[20], facing;
	for (int i = 0; i < 20; i++) {
		xr[i] = i;
		yr[i] = 0;
	}

	while (true) {

		// Сдвиг массивов с координатами 
		if (stop) {
			for (int i = 19; i > 0; i--) {
				xr[i] = xr[i - 1];
				yr[i] = yr[i - 1];
			}
		}

		// Направление
		facing = 0;
		do facing = getkey();
		while ((facing == 1 && xr[0] == 24) || (facing == 2 && yr[0] == 24) || (facing == 3 && xr[0] == 0) || (facing == 4 && yr[0] == 0));
		
		switch (facing) {
			case 1:			// right
				xr[0]++; stop = 1; break;
			case 2:			// down
				yr[0]++; stop = 1; break;
			case 3:			// left
				xr[0]--; stop = 1; break;
			case 4:			// up
				yr[0]--; stop = 1; break;
			case 0:			// nothing
				stop = 0;
				break;
		}

		// Заполнение массива пробелами
		for (int m = 0; m < 25; m++) {
			for (int n = 0; n < 25; n++)
				field[m][n] = ' ';
		}

		// Присваивание главному массиву
		for (int c = 0; c < 20; c++)
			field[yr[c]][xr[c]] = str[c];

		// Вывод массива
		system("cls");
		for (int m = 0; m < 25; m++) {
			for (int n = 0; n < 25; n++) {
				cout << field[m][n];
			}
			cout << endl;
		}
		Sleep(100);
	}
}