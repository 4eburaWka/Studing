#include <iostream>
#include <fstream>
#include "ofb_encr.h"
#include "../Libs/get_time.h"
using namespace std;
/*
int main(){
    string plaintext_str = "The quick brown fox jumps over the lazy dog.";
    string key_str = "k", iv_str = "kikimorawas";

    vector<bitset<16>> plaintext;
    vector<bitset<16>> key, iv;
    for(char el:key_str){
        key.push_back(bitset<16>(el));
    }
    for(char el:plaintext_str){
        plaintext.push_back(bitset<16>(el));
    }
    for(char el:iv_str){
        iv.push_back(bitset<16>(el));
    }
    
    // vector<bitset<16>> ciphertext = permute_encrypt(plaintext, key);
    // vector<bitset<16>> decr_text = permute_decrypt(ciphertext, key);

    vector<bitset<16>> ciphertext = ofb(plaintext, key, iv);
    vector<bitset<16>> decr_text = ofb(ciphertext, key, iv, false);
    string enc;
    for (auto el: ciphertext)
        enc += el.to_int();

    string decrypted_text;
    for (bitset<16> &el: decr_text){
        decrypted_text += el.to_int();
    }

    cout << enc << endl;
    cout << decrypted_text << endl << decrypted_text.length();

}
*/
vector<bitset<16>> get_bitset_vector(string &str){
    vector<bitset<16>> set;
    for (char symb: str)
        set.push_back(bitset<16>(symb));
    return set;
}
string get_string_(vector<bitset<16>> &set){
    string str;
    for(bitset<16> &el: set)
        str += el.to_int();
    return str;
}

int main(){
    int menu; string path, key, iv;
    
    while (true){
        cout << 
        "1. Зашифровать файл, используя ECB." << endl << 
        "2. Дешифровать файл, используя ECB." << endl << 
        "3. Зашифровать файл, используя OFB." << endl << 
        "4. Дешифровать файл, используя OFB." << endl << 
        "5. Выйти из программы." << endl;
        cout << "> "; cin >> menu;

        switch (menu){
            case 3:{
                getline(cin, path);
                cout << "Введите путь к файлу: "; getline(cin, path);
                cout << "Введие пароль: "; getline(cin, key);
                cout << "Введите iv: "; getline(cin, iv);

                ifstream in(path);
                if (in.is_open()) {
                    string plaintext((istreambuf_iterator<char>(in)),
                        (istreambuf_iterator<char>()));

                    vector<bitset<16>> PL_TEXT = get_bitset_vector(plaintext);
                    vector<bitset<16>> KEY = get_bitset_vector(key);
                    vector<bitset<16>> IV = get_bitset_vector(iv);
                    start_clock();
                    vector<bitset<16>> CIPHER = ofb(PL_TEXT, KEY, IV);
                    cout << "Шифрование длилось "; stop_clock(); cout << "c.\n";

                    ofstream out(path+"_ecnr");
                    out << get_string_(CIPHER);
                    out.close();
                } else 
                    cout << "Не удалось открыть файл!\n";
            }
                break;
            case 4:{
                getline(cin, path);
                cout << "Введите путь к файлу: "; getline(cin, path);
                cout << "Введие пароль: "; getline(cin, key);
                cout << "Введите iv: "; getline(cin, iv);

                ifstream in(path);
                if (in.is_open()) {
                    string cipher((istreambuf_iterator<char>(in)),
                        (istreambuf_iterator<char>()));

                    vector<bitset<16>> CIPHER = get_bitset_vector(cipher);
                    vector<bitset<16>> KEY = get_bitset_vector(key);
                    vector<bitset<16>> IV = get_bitset_vector(iv);
                    start_clock();
                    vector<bitset<16>> PL_TEXT = ofb(CIPHER, KEY, IV);
                    cout << "Дешифрование длилось "; stop_clock(); cout << "c.\n";

                    ofstream out(path+"_decr");
                    out << get_string_(PL_TEXT);
                    out.close();
                } else 
                    cout << "Не удалось открыть файл!\n";
            }
                break;
            case 5:{
                return 0;
            }
            break;
        }
    }
}