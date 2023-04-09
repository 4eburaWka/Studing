#include <iostream>

using namespace std;

class Farm{
    public:
        string name;
        int cows, pigs, hens;
        string contacts[10];
    public:
        void TO_SET_NAME(string name){this->name = name;}
        void TO_SET_COWS(int cows){this->cows = cows;}
        void TO_SET_PIGS(int pigs){this->pigs = pigs;}
        void TO_SET_HENS(int hens){this->hens = hens;}

        string TO_GET_NAME(){return this->name;}
        int TO_GET_COWS(){return this->cows;}
        int TO_GET_PIGS(){return this->pigs;}
        int TO_GET_HENS(){return this->hens;}

        Farm(){
            name = "Funny farm";
            cows = 2; pigs = 5; hens = 10;
            contacts[0] = "www.funny-farm.by";
        }
        Farm(string name, int cows, int pigs, int hens){
            this->name = name; this->cows = cows; this->pigs = pigs; this->hens = hens;
        }
        Farm(const Farm &Farm){
            this->name = Farm.name; this->cows = Farm.cows; this->pigs = Farm.pigs; this->hens = Farm.hens;
            for (int i = 0; i < 10; i++)
                this->contacts[i] = Farm.contacts[i];
        }

        void SET_COUNT(string title, int new_count){
            if (title == "cows") this->cows = new_count;
            if (title == "pigs") this->pigs = new_count;
            if (title == "hens") this->hens = new_count;
        }

        void SHOW_INFO(){
            cout << name << "\nWe have " << cows << " cows, " << pigs << " pigs, " << hens << " hens.\nOur contacts:";
            for (int i = 0; i < 10; i++){
                if (contacts[i] != "")
                    cout << "\n" << contacts[i] ;
            }
            cout << "\n";
        }

        void operator++(int){
            this->cows++;
        }
        void operator!(){ // добавить новый контакт
            int t; string new_info;
            cout << "Choose cell that you want to change: "; cin >> t;
            cout << "Enter new contact: "; cin >> new_info;
            this->contacts[t] = new_info;
        }
        bool operator==(const Farm &obj){
            return this->cows == obj.cows && this->pigs == obj.pigs && this->hens == obj.hens;
        }
};

int main(){
    Farm farm1;
    Farm farm2("BrSTU", 186, 5400, 1);
    Farm farm3(farm2);

    farm1.SHOW_INFO();
    cout << (farm2 == farm3) << endl;
    farm2++;
    cout << (farm2 == farm3) << endl;
    !farm2;
    farm2.SHOW_INFO();
}