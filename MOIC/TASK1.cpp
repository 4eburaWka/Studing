#include <iostream>
#include <pSTRING.h>
using namespace std;

class pSTRING
{
private:
    char *str;
    int length;
public:
    pSTRING()
    {
        str = new char[1];
        str[0] = '\0';
        length = 0;
    }
    pSTRING(const char *str)
    {
        length = strlen(str);
        str = new char[length + 1];
        strcpy(str, str);
    }
    pSTRING(const pSTRING &str)
    {
        length = str.length;
        str = new char[length + 1];
        strcpy(str, str.str);
    }
    ~pSTRING()
    {
        delete [] str;
    }
    void SHOW()
    {
        cout << str << endl;
    }
    int SIZE()
    {
        return length;
    }
    bool EMPTY()
    {
        return length == 0;
    }
    pSTRING &ASSIGN(const pSTRING &str)
    {
        if (this == &str)
            return *this;
        delete [] str;
        length = str.length;
        str = new char[length + 1];
        strcpy(str, str.str);
        return *this;
    }
    pSTRING &operator=(const pSTRING &str)
    {
        return ASSIGN(str);
    }
};

int main()
{
    pSTRING str1("Hello");
    pSTRING str2(str1);
    str1.SHOW();
    str2.SHOW();
    cout << str1.SIZE() << endl;
    cout << str2.SIZE() << endl;
    cout << str1.EMPTY() << endl;
    cout << str2.EMPTY() << endl;
    str1.SHOW();
    str1 = str2;
    str1.SHOW();
    return 0;
}
