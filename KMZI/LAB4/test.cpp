#include <iostream>
#include "../Libs/bignumber.h"
using namespace std;
using namespace pr0crustes;

BigNumber sqrt(BigNumber n) { 
    BigNumber x = n; 
    BigNumber y = (x + n / x) / 2; 
    while (y < x) { 
        x = y; 
        y = (x + n / x) / 2; 
    } 
    return x; 
} 
// BigNumber iceil(BigNumber n){
//     if (n % 1 == 0)
//         return n;
//     if (n)
// }

// BigNumber ferma(BigNumber n){
//     BigNumber s = ceil(isqrt(n));
// }


int main(){
    cout << BigNumber("-175") / BigNumber("-87");
}