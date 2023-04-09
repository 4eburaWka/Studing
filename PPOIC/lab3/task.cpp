#include <iostream>
using namespace std;

class First {
    public :
    int amount;
    int& amountref = amount;

    First(int amount, int& amountref) {
        this->amount = amount;
        this->amountref = amountref;
    }
    First() {
        amount = 0;
    }
    First(First& dan) {
        this->amount = dan.amount;
    }
    void TO_SET(int a) {
        this->amount = a;
    }
    void TO_SHOW() {
        cout << "amount = " << amount << endl;
        cout << "amountref = " << amountref << endl;
    }
    int& TO_GET_AMOUNT(int amount) {
        int &a = amount;
        return a;
    }
    void TO_NULL(First & obj) {
        obj.amountref = 0;

    }
    void TO_SQR(First &obj, int &a) {
        obj.amount = a * a;
    }
    void func(int &a){
        a = 232;
    }
    ~First() {
        cout << "1st elelement was deleted" << endl;
    }

    void f1(int a){
        a = 0;
    }
    void f2(int &a){
        a = 0;
    }
    void f3(int *a){
        *a = 0;
    }
};

class Second {
    public:
    int num;
    int& num_ref = num;

    Second(int num) {
        this->num = num;
    }
    Second() {
        num = 0;
    }
    Second(Second& obj) {
        this->num = obj.num;
    }
    void TO_SHOW() {
        cout << "amount : " << num << endl;
        cout << "amountref : " << num_ref << endl;
    }
    void To_Set(int a) {

        this->num = a;
    }
    int &GetSecondtype_plus1(int &a) {
        int b = a+1;
        int &c = b;
        this->num = c;
        return c;
    }
    void power(Second &obj, int &a) {
        obj.num = a * a;
    }

    void TO_NULL(Second& obj) {
    obj.num = 0;
    }
    ~Second() {
        cout << "2st elelement was deleted" << endl;
    }
};

class Third{    
    private:
        string str;    
    public:        
    Third(string str){            
        this->str=str;        
    }        
    Third(){            
        this->str="";        
    }        
    
    Third(Third&ref){            
        this->str=ref.str;        
    }        
    static void TO_CLEAR_STRING(Third&ref){            
        ref.str = "";        
    }        
    void TO_SET(string &temp){            
        this->str = temp;        
    }        
    static int &length(Third&ref){            
        int size = ref.str.length();            
        return size;        
    }        
    void TO_SHOW(){            
        cout << str << endl;        
    }        
    ~Third(){            
        cout<<"3st element was deleted"<<endl;        
    }
};

int main() {
    int a = 5;

    First first(a,a);
    cout << "FIRST\n";
    first.TO_SHOW();
    first.TO_SET(6);
    first.TO_SHOW();
    first.TO_NULL(first);
    first.TO_SHOW(); 
    cout << endl;
    cout << a <<endl;
    first.func(a);
    cout << a << endl;
    first.f1(a); cout << a << endl;a=232;
    first.f2(a); cout << a << endl;a=232;
    first.f3(&a); cout << a << endl << "#####################################" << endl;

    
    Second second(80);
    cout << "SECOND\n";
    second.GetSecondtype_plus1(a);
    second.TO_SHOW();
    second.power(second, a);
    second.TO_SHOW();
    second.TO_NULL(second);
    second.TO_SHOW();
    cout << "#####################################" << endl;

    Third str("Belarus");
    string t="Russia";
    string &ref = t;
    str.TO_SET(t);
    str.TO_SHOW();
    str.TO_CLEAR_STRING(str);
    str.TO_SHOW();

}