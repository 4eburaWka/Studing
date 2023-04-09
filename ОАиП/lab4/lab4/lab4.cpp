#include <iostream>
#include <cstring>
using namespace std;

int main() {
    setlocale(LC_ALL, "ru");
    char str[100], from[10], to[10];
    gets_s(str);
    gets_s(from);
    gets_s(to);
    char* ex = NULL;
    char* pch = strtok_s(str, " ,.-", &ex);
    bool check = true; int num = 0;

    while (check) {
        for (int c = 0; c < strlen(pch); c++) 
            if (pch[c] == from[c]) check = false;
        pch = strtok_s(NULL, " ,.-", &ex);
        num++;
    }
}
