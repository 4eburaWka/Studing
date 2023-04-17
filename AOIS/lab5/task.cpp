#include <iostream>
#include <ctime>
#include <fstream>
#include "windows.h"
using namespace std;

HANDLE hSemaphore;
int a = 1, b = 1, c = 1;

void first(void *pParams){
    srand(time(NULL));
    int s = 0;
    int n = 100;
    while (n)
    {
        s = rand() % 3 + 1;
        WaitForSingleObject(hSemaphore, INFINITE);
        *(int *)pParams = s;
        n--;
    }
    _endthread();
}

int main(void){
    ofstream fout("E:\\Studing\\AOIS\\lab5\\file.txt");

    srand(time(NULL));
    int first_wins = 0, second_wins = 0, third_wins = 0;
    int n = 100;
    _beginthread(first, 0, &a);
    _beginthread(first, 0, &b);
    _beginthread(first, 0, &c);

    hSemaphore = CreateSemaphore(NULL, 3, 3, NULL);

    while (n){
        Sleep(20);
        cout << a << " " << b << " " << c << endl;
        fout << a << " " << b << " " << c << endl;
        switch (a){
        case 1:
            switch (b){
            case 1:
                switch (c){
                case 2:
                    third_wins++;
                    break;
                case 3:
                    first_wins++;
                    second_wins++;
                    break;
                default:
                    break;
                }
                break;
            case 2:
                switch (c){
                case 1:
                    second_wins++;
                    break;
                case 2:
                    second_wins++;
                    third_wins++;
                    break;
                default:
                    break;
                }
                break;
            case 3:
                switch (c){
                case 1:
                    first_wins++;
                    third_wins++;
                    break;
                case 3:
                    first_wins++;
                    break;
                default:
                    break;
                }
                break;
            default:
                break;
            }
            break;
        case 2:
            switch (b){
            case 1:
                switch (c){
                case 1:
                    first_wins++;
                    break;
                case 2:
                    first_wins++;
                    third_wins++;
                    break;
                default:
                    break;
                }
                break;
            case 2:
                switch (c){
                case 1:
                    first_wins++;
                    second_wins++;
                    break;
                case 3:
                    third_wins++;
                    break;
                default:
                    break;
                }
                break;
            case 3:
                switch (c){
                case 2:
                    second_wins++;
                    break;
                case 3:
                    second_wins++;
                    third_wins++;
                    break;
                default:
                    break;
                }
                break;
            default:
                break;
            }
            break;
        case 3:
            switch (b){
            case 1:
                switch (c)
                {
                case 1:
                    second_wins++;
                    third_wins++;
                    break;
                case 3:
                    second_wins++;
                    break;
                default:
                    break;
                }
                break;
            case 2:
                switch (c){
                case 2:
                    first_wins++;
                    break;
                case 3:
                    first_wins++;
                    third_wins++;
                    break;
                default:
                    break;
                }
                break;
            case 3:
                switch (c){
                case 1:
                    third_wins++;
                    break;
                case 2:
                    second_wins++;
                    first_wins++;
                    break;
                default:
                    break;
                }
                break;
            default:
                break;
            }
            break;
        default:
            break;
        }
        ReleaseSemaphore(hSemaphore, 3, NULL);
        n--;
    }
    cout << "1: " << first_wins << "\n2: " << second_wins << "\n3: " << third_wins << endl;
    fout << "1: " << first_wins << "\n2: " << second_wins << "\n3: " << third_wins << endl;
    _endthread();
    CloseHandle(hSemaphore);
    fout.close();
}