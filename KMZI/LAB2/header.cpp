#include <string>
#include <iostream>
#include <bitset>
using namespace std;

void subs(string text, int i, int j, string key){
    char tabl[i][j+1]; int x;
    for (x = 0; x < i; x++)
        tabl[x][j] = '\0';
    while (1){ // удалить пробелы из строки
        x = text.find(' ');
        if (x == -1)
            break;
        text.erase(x, 1);
    }

    for (x = 0; x < text.size(); x++){
        tabl[x % i][x / i] = text[x];
    }
    
    string str;
    for (int o = 0; o < i; o++){
        for (int t = 0; t < j; t++){
            str += tabl[o][t];  
        }
    }
    for (x = 4; x < str.size(); x += 4)
        str.insert(x++, " ");
    cout << str << endl;
}

void subs(bitset<4>)

int main(){
    subs("Thebishoplookedliketheh6squarethencapturedthepawn", 5, 10, " ");
}