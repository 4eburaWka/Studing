#include "..\graphs.h"
#include <iostream>

using namespace std;

int main(){
    List a, b;
    a.append(1);
    a.append(1);
    a.append(1);
    a.append(8);
    a.append(6);

    b.append(1);
    b.append(1);
    b.append(1);
    b.append(8);
    b.append(6);
    cout << (a == b and a==b);
}