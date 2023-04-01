#include "../Libs/bitset.h"
#include "../Libs/vector.h"
#include <iostream>
using namespace std;

vector<unsigned> get_order(vector<bitset<16>> &key){
    // Получить порядок {4, 5, 2, 7}
    vector<unsigned> shadow, order(key.size());
    for(bitset<16> &el: key){
        shadow.push_back(el.to_int());
    }
    unsigned index, cur_num;
    for(int t = 0; t < key.size(); t++){
        cur_num = -1;
        for(int i = 0; i < key.size(); i++){
            if (cur_num >= shadow[i]){
                cur_num = shadow[i];
                index = i;
            }
        }
        order[index] = t;
        shadow[index] = -1;
    }
    return order;
}

vector<bitset<16>> permute_encrypt(vector<bitset<16>> &plaintext, vector<bitset<16>> &key, bool showInfo=true){
    int key_length = key.size();
    while (plaintext.size() % key_length != 0)
        plaintext.push_back(bitset<16>(rand() % 256)); 
    // Шифрование перестановками
    int rows = plaintext.size() / key.size(), columns = key.size();
    vector<vector<bitset<16>>> tabl(rows, vector<bitset<16>>(columns));
    vector<unsigned> order = get_order(key);

    // заполнение tabl 
    for (int x = 0; x < plaintext.size(); x++){
        tabl[x % rows][x / rows] = plaintext[x];
    }
    if (showInfo)
        cout << "33%";

    // перестановка столбцов согласно order
    vector<vector<bitset<16>>> tabl2(rows, vector<bitset<16>>(columns));
    for(int j = 0; j < order.size(); j++){
        for(int i = 0; i < rows; i++){
            tabl2[i][order[j]] = tabl[i][j];
        }
    }
    if (showInfo)
        cout << "\b\b\b66%";

    vector<bitset<16>> ciphertext;
    for (int i = 0; i < rows; i++){
        for (int j = 0; j < columns; j++){
            ciphertext.push_back(tabl2[i][j]);
        }
    }
    if (showInfo)
        cout << "\b\b\b100%" << endl;
    return ciphertext;
}


vector<bitset<16>> permute_decrypt(vector<bitset<16>> &ciphertext, vector<bitset<16>> &key, bool showInfo=true){
    // Расшифрование перестановками
    int rows = ciphertext.size() / key.size(), columns = key.size();
    vector<vector<bitset<16>>> tabl(rows, vector<bitset<16>>(columns));
    vector<unsigned> order = get_order(key);

    // заполнение tabl 
    for (int x = 0; x < ciphertext.size(); x++){
        tabl[x / columns][x % columns] = ciphertext[x];
    }
    if (showInfo)
        cout << "33%" << endl;

    // перестановка столбцов обратно согласно order
    vector<vector<bitset<16>>> tabl2(rows, vector<bitset<16>>(columns));
    for(int j = 0; j < order.size(); j++){
        for(int i = 0; i < rows; i++){
            tabl2[i][j] = tabl[i][order[j]];
        }
    }
    if (showInfo)
        cout << "\b\b\b66%" << endl;
    
    vector<bitset<16>> plaintext;
    for (int i = 0; i < columns; i++){
        for (int j = 0; j < rows; j++){
            plaintext.push_back(tabl2[j][i]);
        }
    }
    if (showInfo)
        cout << "\b\b\b100%" << endl;
    return plaintext;
}