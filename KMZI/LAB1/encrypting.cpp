#include <iostream>
#include <fstream>
using namespace std;

void get_index(char **tabl, int lenI, int lenJ, char symb, int &i, int &j){
    for (i = 0; i < lenI; i++)
        for (j = 0; j < lenJ; j++)
            if (tabl[i][j] == symb)
                return;
    i = -1; j = -1;
}

string encrypt(string path, char **alph){
    ifstream file(path);
    string text, encryptedText;
    int i, j;
    getline(file, text);

    for (int x = 0; x < text.length(); x++){
        get_index(alph, 5, 6, text[x], i, j);
        if (i != -1 and j != -1)
            encryptedText += to_string(i) + to_string(j);
    }

    file.close();
    return encryptedText;
}


int main(){
    string alphabet="abcdefghijklmnopqrstuvwxyz.,? ";
    char **alph;
    alph = new char *[5];
    for (int i = 0; i < 5; i++)
        alph[i] = new char[6];
    for (int i = 0; i < 30; i++){
        alph[i / 6][i % 6] = alphabet[i];
    }

    string path;
    cout << "Введите имя файла: "; getline(cin, path);
    ofstream file(path+"_encr");
    file << encrypt(path, alph);
    cout << "Успешно!";

    file.close();
    for (int i = 0; i < 5; i++)
        delete [] alph[i]; 
    delete [] alph;
}