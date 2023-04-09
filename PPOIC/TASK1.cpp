#include <iostream>
#include <string.h>
using namespace std;

class pSTRING{
    private:
        char *pSTR;
        int length;
        
    public:
        pSTRING(){
            pSTR = new char[1];
            pSTR[0] = '\0';
            length = 0;
        }
        pSTRING(const char *str){
            length = strlen(str);
            pSTR = new char[length + 1];
            strcpy(pSTR, str);
        }
        pSTRING(const pSTRING &str){
            length = str.length;
            pSTR = new char[length + 1];
            strcpy(pSTR, str.pSTR);
        }
        ~pSTRING(){
            delete [] pSTR;
        }
        void SHOW(){
            for (int i = 0; i < length; i++)
                cout << pSTR[i];
            cout << endl;
        }
        int SIZE(){
            return length;
        }
        bool IS_EMPTY(){
            return length == 0;
        }
        pSTRING &ASSIGN(const pSTRING &str){
            if (this == &str)
                return *this;
            delete [] pSTR;
            length = str.length;
            pSTR = new char[length + 1];
            strcpy(pSTR, str.pSTR);
            return *this;
        }
        pSTRING &operator=(const pSTRING &str){
            return ASSIGN(str);
        }
};

int main(){
    pSTRING str1("HOT-DOG");
    pSTRING str2(str1);
    str1.SHOW();
    str2.SHOW();
    
    cout << "Длина строки str1: " << str1.SIZE() << endl;
    cout << "Длина строки str2: " << str2.SIZE() << endl;
    cout << "Строка str2 пуста? : " << str1.IS_EMPTY() << endl;
    cout << "Строка str2 пуста? : " << str2.IS_EMPTY() << endl;
    
    str1.SHOW();
    str1 = str2;
    str1.SHOW();
}

