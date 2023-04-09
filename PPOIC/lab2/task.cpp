#include <iostream>
using namespace std;

class Reader{
    private:
        string books[10];
    public:
        void ADD_BOOK(int cell, string name){
            books[cell] = name;
        }
        void ADD_BOOK(int cell){
            string name;
            cin >> name;
            books[cell] = name;
        }
        void ADD_BOOK(){    
            int cell;
            string name;
            cin >> cell >> name;
            books[cell] = name; 
        }
        void SHOW(){
            for (int i = 0; i < 3; i++)
                cout << books[i];
            cout << endl;
        }
};

class Keyboard{
    public:
        void press(int number){
            cout << "You enter number " << number << endl;
        }
        void press(char symb){
            cout << "You enter symbol " << symb << endl;
        }
        void press(string func){
            cout << "You enter function " << func << endl;
        }
};

class SUM{
    public:
        int sum(int a)
            {return a;}
        
        int sum(int a, int b)
            {return a + b;}
        
        int sum(int a, int b, int c) {return a + b + c;}
};

int main(){
    Reader petya;
    Keyboard kb;
    SUM sum;

    petya.ADD_BOOK(0, "Fizika");
    petya.ADD_BOOK(0);
    petya.ADD_BOOK();
    petya.SHOW();

    kb.press(0);
    kb.press('c');
    kb.press("ctrl");

   cout << "1 " << sum.sum(1) << " 2 " << sum.sum(1, 1) << " 3 " << sum.sum(1,1,1);
}
