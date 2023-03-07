#include <iostream>
#include <fstream>
using namespace std;

int *get_substitution(string path){
    ifstream file(path);
    char numbers[100];
    file >> numbers;
    
    int *substitution, i = 1, t = 1, n = 0, m = 0;

    char temp[] = "00";
    substitution = new int[6];

    while (i < 50){
        while (numbers[i] != ',' && numbers[i] != ']')
            temp[t--] = numbers[i++];
        substitution[n++] = (temp[0] - 48) * 10 + temp[1] - 48;
        temp[0] = '0';
        t = 1; 
        if (numbers[i] == ']')
            break;
        i++;
    }
    return substitution;
}

// 11111111111111111111111111111111111111111111111111
void independentСycles(int *substitution, int *part1, int *part2){
    //независимые циклы
    int flag;
    int p1 = 1, p2 = 1;

    part1[0] = 1;
    while (p1 < 7 && part1[0] != substitution[part1[p1 - 1] - 1]){
        part1[p1++] = substitution[part1[p1 - 1] - 1];
    }
    for (int i = 1; i < 7; i++){
        flag = 0;
        for (int j = 0; j < p1; j++)
            if (part1[j] == i)
                flag = 1;
        if (!flag){
            part2[0] = i;
            while (p2 < 7 && part2[0] != substitution[part2[p2 - 1] - 1]){
                part2[p2++] = substitution[part2[p2 - 1] - 1];
            }
            break;
        }
    }
    cout << "(";
    for (int i = 0; i < p1; i++)
        cout << part1[i] << ",";
    if (!flag){
        cout << "\b)(";
        for (int i = 0; i < p2; i++)
            cout << part2[i] << ",";
    }
    cout << "\b)\n";
}

// 22222222222222222222222222222222222222222222222222
int numberOfTranspositions(int *sub, int n) {
    int substitution[n];
    for (int i = 0; i < n; i++)
        substitution[i] = sub[i];
        
    int count = 0;
    for (int i = 0; i < n; i++) {
        if (substitution[i] != i + 1) {
            int j = i + 1;
            while (substitution[j - 1] != i + 1) {
                j++;
            }
            swap(substitution[i], substitution[j - 1]);
            count++;
        }
    }
    return count;
}


// 33333333333333333333333333333333333333333333333333
int numberOfInversions(int *substitution){
    //количество инверсий
    int inversions = 0;
    for (int i = 0; i < 6; i++)
        for (int j = i + 1; j < 6; j++)
            if (substitution[i] > substitution[j])
                inversions++;
    return inversions;
}

int main(){
setlocale(LC_ALL, "Russian");
    int *a = get_substitution("E:\\Studing\\MOIS\\Lab. 4\\task1");
    int part1[6], part2[6];
    independentСycles(a, part1, part2);

    int transpositions = numberOfTranspositions(a, 6);
    cout << "The substitution is " << (transpositions % 2 == 0 ? "even" : "odd") << " because it has " << transpositions << " transpositions." << endl;    

    int inversions = numberOfInversions(a);
    cout << "The substitution is " << (transpositions % 2 == 0 ? "even" : "odd") << " because it has " << inversions << " inversions." << endl; 
}
