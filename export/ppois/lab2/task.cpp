#include <iostream>
using namespace std;


class Concatenate{
	public:
	string ADD(char a, char b, char c, char d){
		string str;
		str += a; str += b; str += c; str += d;
		return str;
	}
		string ADD(char a, char b, char c){
			string str;
			str += a; str += b; str += c;
			return str;
		}
		string ADD(char a, char b){
			string str;
			str += a; str += b;
			return str;
		}
};


int main(){
	Concatenate STR;

	cout << STR.ADD('1', '2', '3', '4') << endl;
	cout << STR.ADD('1', '2', '3') << endl;
	cout << STR.ADD('1', '2') << endl;
}
