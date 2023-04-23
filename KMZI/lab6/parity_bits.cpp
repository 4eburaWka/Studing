#include <iostream>
#include <bitset>
using namespace std;

bool parity_bit(bitset<8> &bits){
    bool parity = 0;
    for(int i=0; i<8; i++)
        parity ^= bits[i];
    return parity;
}

int main(){
    char data;
    while (true){
        cout << "Enter the data to be transmitted: ";
        cin >> data;

        bitset<8> bits(data);
        cout << "Data: " << bits << ", parity: " << parity_bit(bits) << endl;
    }
}