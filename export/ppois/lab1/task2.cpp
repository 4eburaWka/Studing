#include <iostream>

using namespace std;

class Coordinates{
    private:
        float xyz[3];
    public:
        void TO_SET(float *xyz){
            for (int i = 0; i < 3; i++)
                this->xyz[i] = xyz[i];
        }
        float TO_GET(){
            return *this->xyz;
        }
        Coordinates(){
            for (int i = 0; i < 3; i++)
                xyz[i] = 0;
        }
        Coordinates(float x, float y, float z){
            xyz[0] = x; xyz[1] = y; xyz[2] = z;
        }
        
        void TO_SHOW(){
            cout << '(';
            for (int i = 0; i < 3; i++)
                cout << xyz[i] << ", ";
            cout << "\b\b)\n";
        }

        float &operator[](const int i){
            return xyz[i];
        }
        void operator = (const float *&coordinates){
            for (int i = 0; i < 3; i++)    
                this->xyz[i] = coordinates[i];
        }
        friend Coordinates operator + (Coordinates &coordinates1, Coordinates &coordinates2){
                Coordinates temp;
                for (int i = 0; i < 3; i++)
                    temp[i] = coordinates1[i] + coordinates2[i];
                return temp;
        }
        Coordinates operator*(const int&number){
            Coordinates temp;
            for (int i = 0; i < 3; i++)
                temp[i] = this->xyz[i] * number;
            return temp;
        }
};

int main(){
    Coordinates body1;
    Coordinates body2(4, 48, 4);
    Coordinates body3;

    body1 = {1, -1, 2};
    body3 = body1 + body2;
    body3.TO_SHOW();
    body3 = body3 * 0;
    body3.TO_SHOW();
}