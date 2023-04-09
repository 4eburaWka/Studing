#include <iostream>

using namespace std;

class Vector{
    private:
        float vector[3];
    public:
        void TO_SET(float *vector){
            for (int i = 0; i < 3; i++)
                this->vector[i] = vector[i];
        }
        float TO_GET(){
            return *this->vector;
        }
        void TO_SHOW(){
            cout << '(';
            for (int i = 0; i < 3; i++)
                cout << vector[i] << ", ";
            cout << "\b\b)\n";
        }
        Vector(){
            for (int i = 0; i < 3; i++)
                vector[i] = 0;
        }
        Vector(float one, float two, float three){
            vector[0] = one; vector[1] = two; vector[2] = three;
        }
        float &operator[](const int i){
            return vector[i];
        }
        void operator = (const float *&vector ){
            for (int i = 0; i < 3; i++)    
                this->vector[i] = vector[i];
        }
        Vector operator + (Vector &vector){
            Vector temp;
            for (int i = 0; i < 3; i++)
                temp[i] = this->vector[i] + vector[i];
            return temp;
        }
};

int main(){
    Vector a;
    a = {5,6,7};
    a.TO_SHOW();
    
    Vector b, t;
    b = {1, 1, 1};
    t = b + a;
    t.TO_SHOW();
    for (int i = 0; i < 3; i++)
        cout << t.TO_GET()+i;
}