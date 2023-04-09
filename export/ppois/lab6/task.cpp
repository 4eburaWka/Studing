#include <iostream>
using  std::cout;
using  std::string;
using  std::endl;

namespace  DevicesInOfficeNS {
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
}



namespace EmployeeNS {
	class  Employee :virtual public DevicesInOfficeNS::DevicesInOffice {
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
		Employee(Employee& Sample, DevicesInOffice& Template) {
			this->age = Sample.age;
			this->company = Sample.company;
			this->name = Sample.name;
			this->majority = Sample.majority;
			this->CPU = Template.CPU;
			this->GPU = Template.GPU;
			this->monitor = Template.monitor;
		}
		Employee(Employee& Sample) {
			this->age = Sample.age;
			this->company = Sample.company;
			this->name = Sample.name;
			this->majority = Sample.majority;

		}

		Employee() {
			name = "name wasn't entered";
			company = "company wasn't entered ";
			majority = "majority wasn't entered ";
			age = 0;
		}
		void IntroduceYourself() {
			cout << "Hi,my name is " << name << " I'am " <<
				age << " Y.O. My majority is " << majority << ". I work for " << company << " company!\n\n";
		}
		void Devices() {
			cout << name << " is working on PC with those Devices : \n";
			cout << "Monitor : " << monitor; cout << endl;
			cout << "CPU : " << CPU;; cout << endl;
			cout << "GPU : " << GPU; cout << endl << endl;

		}
	};
}

namespace DeveloperNS {
	class Developer :virtual public EmployeeNS::Employee, virtual public DevicesInOfficeNS::DevicesInOffice {
	public:
		string FavoriteProgrammingLanguage;
		Developer(string name, string company, int age, string majority, string  FavoriteProgrammingLanguage) {
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
		void InitializeDevices(string CPU, string monitor, string GPU) {
			this->CPU = CPU;
			this->GPU = GPU;
			this->monitor = monitor;
		}

		void IntroduceYourself() {
			cout << "Hi,my name is " << name << " I'am " <<
				age << " Y.O. " << majority << ".I work for " << company << " company!\n";
			cout << name << "'s favorite Programming language is " << FavoriteProgrammingLanguage << endl << endl;
		}


	};
}

int main() {
	using  namespace  EmployeeNS; 
	DeveloperNS::Developer Vitya("Vitya", "BSTU", 23, "Programmer", "Turbo C");
	Vitya.IntroduceYourself();
	Employee Kolya("Kolya", "Rybalka", 19, "Rybak");
	Kolya.IntroduceYourself();
	using DevicesInOfficeNS::DevicesInOffice;
	DevicesInOffice KolyasPC("Pentium 4700", "Samsung", "GTX 1050 TI");
	string b = KolyasPC.isstrong(); cout << b <<endl; 
}
