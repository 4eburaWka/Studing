#include <iostream>
using namespace std;

class DevicesInOffice {
public:
	string monitor;
	string CPU;
	string GPU;

	DevicesInOffice() {
		monitor = "";
		CPU = "";
		GPU = "";
	}
	DevicesInOffice(string CPU, string monitor, string GPU) {
		this->CPU = CPU;
		this->GPU = GPU;
		this->monitor = monitor;

	}
	DevicesInOffice(DevicesInOffice& Sample) {
		this->CPU = Sample.CPU;
		this->GPU = Sample.GPU;
		this->monitor = Sample.monitor;
	}

	string isstrong() {
		if (CPU.at(0) == 'P' || CPU.at(0) == 'p') { return "Pc is weak"; }
		else return "Pc is good enough";
	}

};

class  Employee:virtual public DevicesInOffice {
 public:
	string name;
	string company;
	int age;
	string majority;
	Employee(string name, string company, int age, string majority) {
		this->age = age;
		this->company = company;
		this->name = name;
		this->majority = majority;
	};
	Employee(Employee& Sample,DevicesInOffice& Template) {
		this->age = Sample.age;              
		this->company = Sample.company;
		this->name = Sample.name;
		this->majority = Sample.majority; 
		this->CPU = Template.CPU;
		this->GPU = Template. GPU;
		this->monitor = Template.monitor;
	}
	Employee(Employee& Sample) {
		this->age = Sample.age;
		this->company = Sample.company;
		this->name = Sample.name;
		this->majority = Sample.majority;
		
	}

	Employee() {
		name = "";
		company = "";
		majority = "";
		age = 0;
	}
	void Show() {
		cout << "Hi, my name is " << name << " I'am " << 
			age << " Y.O. My majority is " <<majority << ". I work for " << company << " company!\n\n";
	}
	void Devices() {
		cout << name << " is working on PC with those Devices : \n";
		cout << "Monitor : " << monitor; cout << endl;
		cout << "CPU : " << CPU;; cout << endl;
		cout << "GPU : " << GPU; cout << endl << endl;

	}
};

class Developer:virtual public Employee, virtual public DevicesInOffice  {
public:
	string FavoriteProgrammingLanguage;
	Developer(string name, string company, int age, string majority,string  FavoriteProgrammingLanguage) {
		this->age = age;
		this->company = company;
		this->name = name;
		this->majority = majority;
		this->FavoriteProgrammingLanguage = FavoriteProgrammingLanguage;
	};
	Developer(Developer& Sample) {
		this->age = Sample.age;
		this->company = Sample.company;
		this->name = Sample.name;
		this->majority = Sample.majority;
		this->FavoriteProgrammingLanguage = FavoriteProgrammingLanguage;
	}
	Developer() {
		name = "name wasn't entered";
		company = "company wasn't entered ";
		majority = "majority wasn't entered ";
		FavoriteProgrammingLanguage = " Favorite Programming Language wasn't specified";
		age = 0;
	}
	void InitializeDevices (string CPU, string monitor, string GPU) {
		this->CPU = CPU;
		this->GPU = GPU;
		this->monitor = monitor;
	}
	
	void Show() {
		cout << "Hi,my name is " << name << " I'am " <<
			age << " Y.O. " << majority << ".I work for " << company << " company!\n";
		cout << name << "'s favorite Programming language is " << FavoriteProgrammingLanguage<<endl<<endl;
	}
};

int main() { 
	Employee Kolya("Nikolay", "Rybalka", 19, "Rybak");
	DevicesInOffice KolyasDevices("PENTIUM 4700", "DELL 240 HZ ", "NVIDIA GTX 960M");
	Employee Andrey(Kolya, KolyasDevices);
	Andrey.Show(); 
	Andrey.Devices(); string buff = Andrey.isstrong(); cout << buff << endl<<endl;
	
	cout << "##################################\n";

	Developer Vitya ("Vitya", "BSTU", 18, "Programmer","Turbo C");
	Vitya.Employee::Show(); 
	Vitya.Devices();
	Vitya.InitializeDevices("IntelCore I5", "Samsung 144 hz ", "Nvidia 1050 Ti");
	Vitya.Devices();
	buff = Vitya.isstrong(); cout << buff<<endl;

	cout << "##################################\n";

	Vitya.Show();
}