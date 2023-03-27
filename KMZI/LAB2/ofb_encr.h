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
vector<bitset<16>> get_bitset(string &str){
    vector<bitset<16>> set;
    for (char symb: str)
        set.push_back(bitset<16>(symb));
    return set;
}
string get_string(vector<bitset<16>> &set){
    string str;
    for(bitset<16> &el: set)
        str += el.to_int();
    return str;
}


vector<bitset<16>> permute_encrypt(vector<bitset<16>> &plaintext, vector<bitset<16>> &key, bool showInfo=true){
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


vector<bitset<16>> xor_(vector<bitset<16>> &vec1, vector<bitset<16>> &vec2){
    vector<bitset<16>> result(vec1.size());
    for (int i = 0; i < vec1.size(); i++){
        result[i] = vec1[i] ^ vec2[i];
    }
    return result;
}


template <int block_size=11, int block_count=4>
vector<bitset<16>> ofb(vector<bitset<16>> &plaintext, vector<bitset<16>> &key, vector<bitset<16>> &iv, bool showInfo=true){
    vector<bitset<16>> ciphertext, prev_block = iv, prev_block2, block_xor; int i;
    if (showInfo)
        cout << "00%";
    for(i = 0; i < plaintext.size() - block_size + 1; i += block_size){
        prev_block2 = permute_encrypt(prev_block, key, false);
        vector<bitset<16>> block(plaintext, i, block_size);
        block_xor = xor_(block, prev_block2);
        ciphertext.insert(block_xor);
        prev_block = prev_block2;
        if (showInfo)
            cout << "\b\b\b" << (int)(i / plaintext.size() * 100) << "%";
    }
    if (plaintext.size() % block_size != 0){
        // int last_block_size = plaintext.size() % block_size;
        // vector<bitset<16>> last_block(block_size);
        // copy(plaintext.end()-last_block_size, plaintext.end(), last_block.begin());
        // prev_block2 = permute_encrypt(prev_block, key, false);
        // block_xor = xor_(last_block, prev_block2);
        // ciphertext.insert(block_xor);
        ciphertext.insert(plaintext.subvector(i, plaintext.size() % block_size));
    }
    if (showInfo)
        cout << "\b\b\b100%" << endl;
    return ciphertext;
}


