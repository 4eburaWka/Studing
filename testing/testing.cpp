#include <iostream>
#include <conio.h>
#include <fstream>
#include <windows.h>
#include <cmath>
using namespace std;

//Структура «Информация»: носитель; объем; название; автор.

enum { _Name, _Brand, _Type, _Size };
struct INFO {
	char Name[40], Brand[40];
	int type, size, tsize;
};

void Menu(), NewFile(char*), ItemAdd(char*), Output(char*), Delete(char*), Sort(char*);
void mergesort(INFO*&, int, int), mergesort_r(int, int, INFO*&, int), merge(INFO*&, int, int, int, int, int);
void Read(ifstream&, INFO&), Write(ofstream&, INFO&), Resize(INFO*&, int), infoAdd(INFO&), typeAdd(INFO&), sizeAdd(INFO&);

void(*TaskList[])(char*) = { NewFile,ItemAdd,Output,Delete,Sort };

void Task(), Rand(char*, int, int, int), MatrOut1(char*, int, int), MatrOut2(char*, int), Transport(char*, char*, int, int);

void(*Work[])() = { Menu,Task };

int main()
{
	SetConsoleCP(1251);
	SetConsoleOutputCP(1251);
	int select;
	cout << "what task u want?";
	do {
		select = _getch() - '1';
	} while (select > 1 || select < 0);
	system("cls");
	Work[select]();
	return 0;
}

void Menu()
{
	int input;
	char name[40];
	NewFile(name);
	do {
		cout << "1.Create file" << endl;
		cout << "2.Add to file" << endl;
		cout << "3.Output" << endl;
		cout << "4.Removing" << endl;
		cout << "5.Sorting" << endl;
		cout << "0.Exit" << endl;
		do {
			input = _getch() - '0';
		} while (input < 0 || input>5);
		system("cls");
		if (!input)
			break;
		else
			TaskList[--input](name);
	} while (true);
}
void NewFile(char* name)
{
	ofstream fout;
	cout << "The name of file: "; cin >> name;
	fout.open(name, ios::trunc | ios::binary);
	if (fout.is_open())
		cout << "File was created!" << endl;
	else
		cout << "Error!" << endl;
	fout.close();
	system("pause");
	system("cls");
}
void ItemAdd(char* name)
{
	ofstream fout;
	INFO list;
	infoAdd(list);
	typeAdd(list);
	sizeAdd(list);
	fout.open(name, ios::binary | ios::app);
	Write(fout, list);
	fout.close();
	system("pause");
	system("cls");
}
void infoAdd(INFO& list)
{
	cout << "The name of nositel: ";	cin >> list.Name;
	cout << "The name of breend: ";	cin >> list.Brand;
	system("cls");
}
void typeAdd(INFO& list)
{
	bool OK = false;
	cout << "Type of nositel:\n";
	cout << "1.HDD\n";
	cout << "2.SSD\n";
	cout << "3.Floppy\n";
	cout << "4.Flash\n";
	cout << "5.CD\n";
	cout << "6.MicroSD\n";
	do {
		OK = true;
		switch (_getch())
		{
		case '1': list.type = 0; break;
		case '2': list.type = 1; break;
		case '3': list.type = 2; break;
		case '4': list.type = 3; break;
		case '5': list.type = 4; break;
		case '6': list.type = 5; break;
		default: OK = false;
		}
	} while (!OK);
	system("cls");
}
void sizeAdd(INFO& list)
{
	bool OK = false;
	cout << "Capacity of nositel: "; cin >> list.size;
	cout << "edinica izmereniya:\n";
	cout << "1.MB\n";
	cout << "2.GB\n";
	cout << "3.TB\n";
	do {
		OK = true;
		switch (_getch())
		{
		case '1': list.tsize = 0; break;
		case '2': list.tsize = 1; break;
		case '3': list.tsize = 2; break;
		default: OK = false;
		}
	} while (!OK);
	system("cls");
}
void Output(char* name)
{
	char type[][8] = { "HDD", "SSD", "Floppy", "Flash", "CD","MicroSD" };
	char tsize[][3] = { "MB","GB","TB" };
	ifstream fin;
	INFO list;
	fin.open(name);
	for (int num = 1; !fin.eof(); num++)
	{
		Read(fin, list);
		if (fin.eof())
			break;
		cout << '#' << num << endl;
		cout << "Name: " << list.Name << endl;
		cout << "Brend: " << list.Brand << endl;
		cout << "type of nositel: " << type[list.type] << endl;
		cout << "Capacity: " << list.size << ' ' << tsize[list.tsize] << endl;
	}
	fin.close();
	system("pause");
	system("cls");
}
void Delete(char* name)
{
	INFO list;
	ifstream fin;
	ofstream fout;
	int num;
	do {
		cout << "input number: "; cin >> num;
	} while (num < 1);
	fin.open(name, ios::binary);
	fout.open("buff.bin", ios::trunc | ios::binary);
	for (int i = 1; !fin.eof(); i++)
	{
		Read(fin, list);
		if (i != num && !fin.eof())
			Write(fout, list);
	}
	fin.close();
	fout.close();
	remove(name);
	rename("buff.bin", name);
	system("cls");
}
void Sort(char* name)
{
	int len = 0, param;
	ifstream fin;
	INFO* list = new INFO[len];
	fin.open(name, ios::in | ios::binary);
	do
	{
		Resize(list, len);
		Read(fin, list[len++]);
	} while (!fin.eof());
	Resize(list, len--);
	fin.close();
	cout << "kak otsortirovat?\n";
	cout << "1.name of nositel\n2.brend\n3.type of nositel\n4.capacity\n";
	do {
		param = _getch() - '0';
	} while (param < 1 || param > 4);
	system("cls");
	mergesort(list, len, --param);
	ofstream fout;
	fout.open(name, ios::trunc | ios::binary);
	for (int i = 0; i < len; i++) Write(fout, list[i]);
	delete[] list;
}
void merge(INFO*& list, int left_start, int left_end, int right_start, int right_end, int param)
{
	int left_length = left_end - left_start;
	int right_length = right_end - right_start;

	INFO* left_half = new INFO[left_length];
	INFO* right_half = new INFO[right_length];

	int r = 0;
	int l = 0;
	int i = 0;

	for (i = left_start; i < left_end; i++, l++)
	{
		left_half[l] = list[i];
	}

	for (i = right_start; i < right_end; i++, r++)
	{
		right_half[r] = list[i];
	}

	for (i = left_start, r = 0, l = 0; l < left_length && r < right_length; i++)
	{
		switch (param)
		{
		case _Name:
			if (strcmp(left_half[l].Name, right_half[r].Name) < 0) { list[i] = left_half[l++]; }
			else { list[i] = right_half[r++]; }
			break;
		case _Brand:
			if (strcmp(left_half[l].Brand, right_half[r].Brand) < 0) { list[i] = left_half[l++]; }
			else { list[i] = right_half[r++]; }
			break;
		case _Type:
			if (left_half[l].type < right_half[r].type) { list[i] = left_half[l++]; }
			else { list[i] = right_half[r++]; }
			break;
		case _Size:
			if (left_half[l].size * pow(1024, left_half[l].tsize) < right_half[r].size * pow(1024, right_half[r].tsize)) { list[i] = left_half[l++]; }
			else { list[i] = right_half[r++]; }
			break;
		}
	}

	for (; l < left_length; i++, l++) { list[i] = left_half[l]; }
	for (; r < right_length; i++, r++) { list[i] = right_half[r]; }
	delete[] left_half;
	delete[] right_half;
}
void mergesort_r(int left, int right, INFO*& list, int param)
{
	if (right - left <= 1)
	{
		return;
	}

	int left_start = left;
	int left_end = (left + right) / 2;
	int right_start = left_end;
	int right_end = right;

	mergesort_r(left_start, left_end, list, param);
	mergesort_r(right_start, right_end, list, param);

	merge(list, left_start, left_end, right_start, right_end, param);
}
void mergesort(INFO*& list, int length, int param)
{
	mergesort_r(0, length, list, param);
}
void Read(ifstream& fin, INFO& list)
{
	fin.read(list.Name, sizeof(char) * 40), fin.read(list.Brand, sizeof(char) * 40),
		fin.read((char*)&list.type, sizeof(int)), fin.read((char*)&list.size, sizeof(int)), fin.read((char*)&list.tsize, sizeof(int));
}
void Write(ofstream& fout, INFO& list)
{
	fout.write(list.Name, sizeof(char) * 40), fout.write(list.Brand, sizeof(char) * 40),
		fout.write((char*)&list.type, sizeof(int)), fout.write((char*)&list.size, sizeof(int)), fout.write((char*)&list.tsize, sizeof(int));
}
void Resize(INFO*& list, int size)
{
	INFO* temp = new INFO[size + 1];
	for (int i = 0; i < size; i++) temp[i] = list[i];
	if (size) delete[] list;
	list = temp;
}

void Task()
{
	int k, m, n;
	char name1[40], name2[40];
	NewFile(name1), NewFile(name2);
	cout << "kakaya razmernost MxN: "; cin >> m >> n;
	cout << "how many matrixs generate: "; cin >> k; Rand(name1, k, m, n);
	Transport(name1, name2, m, n);
	system("cls");
	cout << name1 << endl << endl; MatrOut1(name1, m, n);
	cout << name2 << endl << endl; MatrOut2(name2, n);
}
void Rand(char* name, int count, int m, int n)
{
	ofstream fout;
	int temp;
	fout.open(name, ios::binary | ios::trunc);
	for (int i = 0; i < count; i++)
	{
		for (int j = 0; j < m * n; j++)
		{
			temp = rand() % 10;
			fout.write((char*)&temp, sizeof(int));
		}
		for (int j = 0; j < m; j++)
		{
			temp = rand() % 10;
			fout.write((char*)&temp, sizeof(int));
		}
	}
	fout.close();
}
void MatrOut1(char* name, int m, int n)
{
	ifstream fin;
	int temp = 0;
	fin.open(name, ios::binary);
	while (!fin.eof())
	{
		for (int i = 0; i < m; i++)
		{
			for (int j = 0; j < n; j++)
			{
				fin.read((char*)&temp, sizeof(int));
				if (fin.eof()) break;
				cout << temp << ' ';
			}
			if (fin.eof()) break;
			cout << endl;
		}
		if (fin.eof()) break;
		cout << endl;
		for (int i = 0; i < m; i++)
		{
			fin.read((char*)&temp, sizeof(int));
			cout << temp << endl;
		}
		cout << endl;
	}
	system("pause");
	system("cls");
}
void MatrOut2(char* name, int n)
{
	ifstream fin;
	int temp = 0;
	fin.open(name, ios::binary);
	while (!fin.eof())
	{
		for (int j = 0; j < n; j++)
		{
			fin.read((char*)&temp, sizeof(int));
			if (fin.eof()) break;
			cout << temp << endl;
		}
		if (fin.eof()) break;
		cout << endl;
	}
	system("pause");
	system("cls");
}
void Transport(char* name1, char* name2, int m, int n)
{
	int** Matr1 = new int* [m];
	for (int i = 0; i < m; i++) Matr1[i] = new int[n];
	int* Matr2 = new int[m];
	ifstream fin;
	ofstream fout;
	int temp;
	fin.open(name1, ios::binary);
	fout.open(name2, ios::binary | ios::trunc);
	while (!fin.eof())
	{
		for (int i = 0; i < m; i++)
		{
			for (int j = 0; j < n; j++)
			{
				fin.read((char*)&Matr1[i][j], sizeof(int));
				if (fin.eof()) break;
				cout << Matr1[i][j] << ' ';
			}
			if (fin.eof()) break;
			cout << endl;
		}
		if (fin.eof()) break;
		cout << endl;
		for (int i = 0; i < m; i++)
		{
			fin.read((char*)&Matr2[i], sizeof(int));
		}
		for (int i = 0; i < n; i++)
		{
			temp = 0;
			for (int j = 0; j < m; j++)
			{
				temp += Matr1[j][i] * Matr2[j];
				cout << Matr1[j][i] << " * " << Matr2[j] << " = " << Matr1[j][i] * Matr2[j] << " -> ";
				cout << temp << endl;
			}
			cout << endl;
			fout.write((char*)&temp, sizeof(int));
		}
		if (fin.eof())
			cout << "file ended!";
	}
	for (int i = 0; i < m; i++)
		delete[] Matr1[i];
	delete[] Matr1;
	delete[] Matr2;
	fin.close();
	fout.close();
}
