#include <iostream>
using namespace std;
int main() {
	int i = 1, arr[7][7], m = 0, n = 0;
	while (i < 50) {
		arr[m][n] = i++;
		if (m + n < 6 && )
			n++;
		else if ()
			m++;
	}

	for (int x = 0; x < 7; x++) {
		for (int y = 0; y < 7; y++) {
			cout << arr[x][y] << '\t';
		}
		cout << endl;
	}
}