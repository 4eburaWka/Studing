#include <iostream>
#include <fstream>
using namespace std;

int get_count(string str, char symb){
    int count = 0;
    for (char el: str)
        if (el == symb)
            count++;
    return count;
}   

string compress(string path){
    ifstream file(path);
    string text, all_symbs;
    getline(file, text);

    for (char i: text)
        if (text.find(i) == -1)
            all_symbs += i;
    
    string symbCode[all_symbs.length()];
    int 
    for (char i: all_symbs){

    }
}

int main(){
    string path;
    cout << "Введите имя файла: "; getline(cin, path);
    ofstream file(path+"_comp");
    file << compress(path);
    cout << "Успешно!";
}