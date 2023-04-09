#include <iostream>
#include <math.h>
using namespace std;

class First{
    private:
        int a;
        int &aRef;
    public:
        First(int a, int &aRef) : a(a), aRef(aRef) {}
        First() : a(0), aRef(a) {}
        First(First& obj) : a(obj.a), aRef(a) {}
        void TO_SET(int a) {
            this->a = a;
        }
        void TO_SHOW() {
            cout << "a = " << a << endl;
            cout << "aRef = " << aRef << endl;
        }
        int& TO_GET_A(int a) {
            int &aRef = a;
            return aRef;
        }
        void TO_NULL(First & obj) {
            obj.aRef = 0;
        }
        void TO_SQR(First &obj, int &a) {
            obj.a = a * a;
        }
        void func(int &a){
            a = 232;
        }
        ~First() {
            cout << "1st was deleted" << endl;
        }
        void function1(int x){
            x = 0;
        }
        void function2(int &x){
            x = 0;
        }
        void function3(int *x){
            *x = 0;
        }
};

class Second {
    private:
        int num;
        int& num_ref = num;

    public:
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
        void exp(Second &obj, int &a) {
            obj.num = pow(2.72, a);
        }

        void TO_NULL(Second& obj) {
            obj.num = 0;
        }
        ~Second() {
            cout << "2st was deleted" << endl;
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
            int c = ref.str.length();
            int &size = c;            
            return size;        
        }        
        void TO_SHOW(){            
            cout << str << endl;        
        }        
        ~Third(){            
            cout<<"3st element was deleted"<<endl;        
        }
};

int main(){
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
    first.function1(a); cout << a << endl;a=232;
    first.function2(a); cout << a << endl;a=232;
    first.function3(&a); cout << a << endl;
    cout << "#####################################" << endl;


    Second second(80);
    cout << "SECOND\n";
    second.GetSecondtype_plus1(a);
    second.TO_SHOW();
    second.exp(second, a);
    second.TO_SHOW();
    second.TO_NULL(second);
    second.TO_SHOW();
    cout << "#####################################" << endl;


    Third str("Belarus");
    string t="Russia";
    string &ref = t;
    str.TO_SET(ref);
    str.TO_SHOW();
    str.TO_CLEAR_STRING(str);
    str.TO_SHOW();
}