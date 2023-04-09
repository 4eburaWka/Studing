#include <iostream>
using namespace std;

class Person{
    private:
        string name;
        int age;
        bool isMan;
    public:
        friend void setName(Person&, string);
        friend void setAge(Person&, int);
        friend void setGender(Person&, bool);

        Person() { name = ""; age = 0; isMan = true; }
        Person(string name, int age, bool isMan) { this->name = name; this->age = age; this->isMan = isMan; }
        Person(Person& per) { name = per.name; age = per.age; isMan = per.isMan; }

        void TO_SHOW(){
            cout << "Name: " << name << endl;
            cout << "Age: " << age << endl;
            if (isMan)
                cout << "MAN" << endl;
            else 
                cout << "woman" << endl;
        }

        friend bool operator==(Person& per1, Person& per2) {
            if (per1.age == per2.age) 
                return true;
            else 
                return false;
        }
        friend void operator!(Person& per) {
            per.isMan = !per.isMan;
        }
        friend void operator+(Person &per, string name) {
            per.name = name;
        }
};

void setName(Person& p, string name){
    p.name = name;
}
void setAge(Person& p, int age){
    p.age = age;
}
void setGender(Person& p, bool isMan){
    p.isMan = isMan;
}


class array{
    private:
        int *arr, size;
    public:
        array() {
            size = 0;
            arr = new int[size];
        }
        array(int size, int *arr) {
            this->size = size;
            this->arr = new int[size];
            for (int i = 0; i < size; i++)
                this->arr[i] = arr[i];
        }
        array(const array& arr2) {
            this->size = arr2.size;
            this->arr = new int[size];
            for (int i = 0; i < size; i++)
                this->arr[i] = arr2.arr[i];
        }
        void TO_SHOW() {
            for (int i = 0; i < size; i++)
                cout << arr[i] << " ";
            cout << endl;
        }

        friend void setArr(array& ar, int *arr);
        friend void setSize(array& ar, int size);
        friend int lastindex(array &ar, int size);

        friend int operator+(array& arr1, array& arr2) {
            int sum = 0;
            for (int i = 0; i < arr1.size; i++)
                sum += arr1.arr[i];
            for (int i = 0; i < arr2.size; i++)
                sum += arr2.arr[i];
            return sum;
        }
        friend int operator-(array& arr1, array& arr2) {
            int sum = 0;
            for (int i = 0; i < arr1.size; i++)
                sum += arr1.arr[i];
            for (int i = 0; i < arr2.size; i++)
                sum -= arr2.arr[i];
            return sum;
        }
        friend void operator!(array& arr) {
            for (int i = 0; i < arr.size; i++)
                cout << arr.arr[i] << ", ";
        }
};
void setArr(array& ar, int *arr){
    ar.arr = arr;
}
void setSize(array& ar, int size){
    ar.size = size;
}
int lastindex(array &ar, int size){
    return size - 1;
}


class Clothes{
    private:
        string name;
        int size;
        string color;
    public:
        Clothes() { name = ""; size = 0; color = ""; }
        Clothes(string name, int size, string color) { this->name = name; this->size = size; this->color = color; }
        Clothes(Clothes& clo) { name = clo.name; size = clo.size; color = clo.color; }

        void TO_SHOW() {
            cout << "Name: " << name << endl;
            cout << "Size: " << size << endl;
            cout << "Color: " << color << endl;
        }

        friend void setName(Clothes& clo, string name);
        friend void setSize(Clothes& clo, int size);
        friend void setColor(Clothes& clo, string color);
};

void setName(Clothes& clo, string name) {
    clo.name = name;
}
void setSize(Clothes& clo, int size) {
    clo.size = size;
}
void setColor(Clothes& clo, string color) {
    clo.color = color;
}

int main(){
    Person Vasya;
    setName(Vasya, "Vasya");
    setAge(Vasya, 20);
    setGender(Vasya, true);
    Vasya.TO_SHOW();
    Person Masha("Masha", 20, false);
    cout << "Masha and Vasya are peers: " << (Vasya == Masha) << endl;
    !Masha; Masha + "MARIA";
    Masha.TO_SHOW();

    cout << "#####################################################" << endl;

    array array1(5, new int[5]{1, 2, 3, 4, 5});
    array array2(5, new int[5]{6, 7, 8, 9, 10});
    cout << "Sum of arrays: " << array1 + array2 << endl;
    cout << "Difference of arrays: " << array1 - array2 << endl;
    cout << "Array1: "; !array1; cout << endl;

    cout << "#####################################################" << endl;

    Clothes Tshirt;
    setName(Tshirt, "T-shirt");
    setSize(Tshirt, 42);
    setColor(Tshirt, "white");
    Tshirt.TO_SHOW();
}