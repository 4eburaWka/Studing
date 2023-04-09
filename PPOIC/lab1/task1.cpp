#include <iostream>

using namespace std;

class Reader{
    private:
        bool isFree[10]= {true, true, true, true, true, true, true, true, true, true};
        string name, surname, patronymic;
        int number;
        string books[10];
    public:
        void TO_SET_NAME(string name){this->name = name;}
        void TO_SET_SURNAME(string surname){this->surname = surname;}
        void TO_SET_PATRONYMIC(string patronymic){this->patronymic = patronymic;}
        void TO_SET_NUMBER(int number){this->number = number;}

        string TO_GET_NAME(){return this->name;}
        string TO_GET_SURNAME(){return this->surname;}
        string TO_GET_PATRONYMIC(){return this->patronymic;}
        int TO_GET_NUMBER(){return this->number;}

        Reader(){
            name = "Vasya";
            surname = "Vasilev";
            patronymic = "Vladimirovich";
            number = 1;
        }
        Reader(string name, string surname, string patronymic, int number){
            this->name = name; this->surname = surname; this->patronymic = patronymic; this->number =number;
        }
        Reader(const Reader &Reader){
            this->name = Reader.name;
            this->surname = Reader.surname;
            this->patronymic = Reader.patronymic;            
            for (int i = 0; i < 10; i++){
                this->isFree[i] = Reader.isFree[i];
                this->books[i] = Reader.books[i];
            }
        }
        string takeBook(string name){
            for (int i = 0; i < 10; i++){
                if (isFree[i] == true){
                    this -> books[i] = name;
                    isFree[i] = false;
                    return "Success";
                }
            }
            return "You already have 10 books!";
        }
        string returnBook(string name){
            for (int i = 0; i < 10; i++){
                if (books[i] == name){
                    books[i] = "";
                    isFree[i] == true;
                    return "Success";
                }
            }
            return "There is no such book";
        }

        void SHOW_BOOKS(){
            int y = 0;
            for (int i = 0; i < 10; i++)
                if (isFree[i] == false)
                    cout << books[i] << endl;
                else y++;
            if (y == 10) cout << "This reader has no books\n";
        }
        void operator = (const int &new_number){
            this->number = new_number;
        }
        void operator + (const int &number){
            if (isFree[number] == true){
                isFree[number] = false;
                cout << "Enter the name of the book : "; cin >> books[number];
            } else cout << "This cell is already taken";
        }
        void operator! (){ //удалить все книги
            for (int i = 0; i < 10; i++){
                isFree[i] = true;
                books[i] = "";
            }
        }
};
int main(){
    Reader a;
    Reader b("Timofei", "Litvinyuk", "Vladimirovich", 5);
    a + 3; // в 3 ячейку поместить книгу
    a.SHOW_BOOKS();
    Reader c(a);
    c.SHOW_BOOKS();
    !c; // удалить все книги
    c.SHOW_BOOKS();
}