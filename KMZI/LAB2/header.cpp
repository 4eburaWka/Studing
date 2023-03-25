#include <iostream>
#include <vector>
#include <bitset>
using namespace std;

template <size_t rows, size_t columns>
void subs2(vector<bitset<8>> &text, vector<bitset<8>> &key){
    vector<vector<bitset<8>>> tabl(rows, vector<bitset<8>>(columns, bitset<8>("0")));
    for (int x = 0; x < text.size(); x++){
        tabl[x % rows][x / rows] = text[x];
    }
    for (int i = 0; i < rows; i++){
        for (int j = 0; j < columns; j++){
            cout << tabl[i][j] << " ";
        }
        cout << endl;
    }
}

int main(){
    string str = "The bishop looked like the h6 square then captured the pawn"; int x;
    while (1){ // удалить пробелы из строки
        x = str.find(' ');
        if (x == -1)
            break;
        str.erase(x, 1);
    }
    
    vector<bitset<8>> text(str.begin(), str.end());
    vector<bitset<8>> key(4, bitset<8>("01101001"));
    subs2<4, 10>(text, key);
}