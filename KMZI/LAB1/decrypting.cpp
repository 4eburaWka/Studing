#include <fstream>
#include <iostream>
using namespace std;

string decrypt(string cipher, char **alph){
    string decryptedText;

    for (int x = 0; x < cipher.length(); x += 2){
        int index_i = cipher[x] - '0';
        int index_j = cipher[x+1] - '0';
        decryptedText += alph[index_i][index_j];
    }
    return decryptedText;
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

    string path, encryptedText;
    cout << "Введите имя файла: "; getline(cin, path);
    ifstream file(path);
    getline(file, encryptedText);
    cout << decrypt(encryptedText, alph);

    file.close();
    for (int i = 0; i < 5; i++)
        delete [] alph[i]; 
    delete [] alph;
}