#include <iostream>
#include <bitset>
using namespace std;

int main() {
    std::string str = "пивас"; // Исходная строка
    std::bitset<8> bit_seq; // Создание пустой битовой последовательности размером 8
    std::string binary_str, part, full; // Создание пустой строки для хранения бинарного представления
    for (size_t i = 0; i < str.size(); i++) {
        bit_seq = std::bitset<8>(str[i]); // Создание битовой последовательности из i-го символа строки
        binary_str += bit_seq.to_string(); // Добавление бинарного представления i-го символа в конец строки
    }
    std::cout << binary_str << std::endl; // Вывод строки из 0 и 1

    for (int i = 0; i < binary_str.size(); i+=8){
        part = "";
        for (int j = i; j < i+8; j++){
            part += binary_str[j];
        }
        cout << part;
        full += bitset<8>(part).to_ulong();
    }
    cout << endl << endl << full;
}