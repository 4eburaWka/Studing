#include <vector>
#include <iostream>
#include <string>
using namespace std;

int main(){
    vector<bool> a;  int c=0;
    string str = "111110001010110", str2 = "101010101010101", str3 = "011001100110011", str4 = "000111100001111", str5="000000011111111";
    for (int i = 0; i < 15; i++){
        if (str[i] == '1' && str2[i] == '1')
            c++;
    }
    cout << c;
    
}

// 111110001010110