#include <iostream>
#include <vector>
#include <bitset>
using namespace std;

// Permutation cipher function
vector<bitset<8>> permute(vector<bitset<8>> &text, vector<int> &order) {
    vector<bitset<8>> permuted(text.size());
    for (int i = 0; i < text.size(); i++) {
        int index = order[i % order.size()];
        permuted[index] = text[i];
    }
    return permuted;
}

// Permutation cipher decryption function
vector<bitset<8>> permute_decrypt(vector<bitset<8>> text, vector<int> order) {
    vector<bitset<8>> permuted(text.size());
    for (int i = 0; i < text.size(); i++) {
        int index = order[i % order.size()];
        permuted[i] = text[index];
    }
    return permuted;
}

// OFB function
template <int rows, int columns>
vector<bitset<8>> ofb(vector<bitset<8>> &text, vector<bitset<8>> &key, bitset<8> iv, vector<int> order, vector<bitset<8>> (*permutation)(vector<bitset<8>> &, vector<int> &)) {
    vector<vector<bitset<8>>> tabl(rows, vector<bitset<8>>(columns, bitset<8>("0")));
    for (int x = 0; x < text.size(); x++){
        tabl[x % rows][x / rows] = text[x];
    }
    
    vector<bitset<8>> keystream;
    bitset<8> prev = iv;
    for (int i = 0; i < rows; i++){
        bitset<8> output = tabl[i][0] ^ key[i];
        keystream.push_back(output);
        for (int j = 1; j < columns; j++){
            output = tabl[i][j] ^ output;
            keystream.push_back(output);
        }
    }
    
    vector<bitset<8>> ciphertext = permutation(text, order); // perform permutation
    for (int i = 0; i < text.size(); i++) {
        ciphertext[i] ^= keystream[i];
    }
    
    for (int i = 0; i < rows; i++){
        for (int j = 0; j < columns; j++){
            cout << tabl[i][j] << " ";
        }
        cout << endl;
    }
    
    cout << "Keystream: ";
    for (int i = 0; i < keystream.size(); i++) {
        cout << keystream[i];
    }
    cout << endl;
    
    cout << "Ciphertext: ";
    for (int i = 0; i < ciphertext.size(); i++) {
        cout << ciphertext[i];
    }
    cout << endl;
    
    return ciphertext;
}

template <size_t rows, size_t columns>
vector<bitset<8>> ofb_decrypt(vector<bitset<8>> &text, vector<bitset<8>> &key, bitset<8> &iv, vector<int> &order, vector<bitset<8>> (*permutation)(vector<bitset<8>>, vector<int>)) {
    vector<bitset<8>> decrypted(text.size(), bitset<8>("0"));
    vector<bitset<8>> keystream(rows * columns, bitset<8>("0"));
    keystream[0] = permutation({iv}, order)[0];
    for (int i = 1; i < keystream.size(); i++) {
        keystream[i] = permutation({keystream[i - 1]}, order)[0];
    }
    for (int i = 0; i < text.size(); i++) {
        if (i > 0 && i % (rows * columns) == 0) {
            keystream[0] = permutation({keystream[rows * columns - 1]}, order)[0];
            for (int j = 1; j < keystream.size(); j++) {
                keystream[j] = permutation({keystream[j - 1]}, order)[0];
            }
        }
        decrypted[i] = text[i] ^ keystream[i % (rows * columns)];
    }
    return decrypted;
}


int main() {
    string str = "The bishop looked like the h6 square then captured the pawn"; int x;
    while (1){ // remove spaces from the string
        x = str.find(' ');
        if (x == -1)
            break;
        str.erase(x, 1);
    }
    
    vector<bitset<8>> text(str.begin(), str.end());
    vector<bitset<8>> key(4, bitset<8>("01101001"));
    vector<int> order = {3, 2, 6, 0, 1, 7, 5, 4};
    bitset<8> iv("10101010");

    // Encrypt using OFB with permutation cipher
    ofb<4, 11>(text, key, iv, order, permute);
}