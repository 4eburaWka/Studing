#include "./permutation.h"
#include <iostream>
using namespace std;


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


