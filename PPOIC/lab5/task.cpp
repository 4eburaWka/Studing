#include <iostream>
using namespace std;

class Tree{
	public:
		string nameOfTree;
		int age, reliability;

		Tree(){
			nameOfTree = "";
			age = 0;
			reliability = 0;
		}
		Tree(string n, int a, int r){
			nameOfTree = n;
			age = a;
			reliability = r;
		}
		Tree(Tree &t){
			nameOfTree = t.nameOfTree;
			age = t.age;
			reliability = t.reliability;
		}

		void TO_SET(int a, int r, string n){
			age = a; reliability = r; nameOfTree = n;
		}

		bool isReliable(){
			if(reliability > 50)
				return true;
			return false;
		}

		void TO_SHOW(){
			cout << "nameOfTree: " << nameOfTree << endl;
			cout << "age: " << age << "\nreliability: " << reliability << endl;
		}
};

class Door{
	public:
		int height, width; string model;
		Door(){
			model = "";
			height = 0;
			width = 0;
		}
		Door(string m, int h, int w){
			model = m;
			height = h;
			width = w;
		}
		Door(Door &d){
			this->model = d.model;
			this->height = d.height;
			this->width = d.width;
		}
		void TO_SET(int h, int w){
			height = h; width = w;
		}
		void TO_SET(string m){
			model = m;
		}

		void TO_SHOW2(){
			cout << "Furniture: Door" << endl;
			cout << "Model: " << model << endl;
			cout << "Height: " << height << endl;
			cout << "Width: " << width << endl;
		}
};

class cupboard : public Door, public Tree{
	public:
		cupboard():Tree(), Door(){}
		cupboard(string nameOfTree, int age, int reliability, 
				int height, int width, string model):Tree(nameOfTree, age, reliability), Door(model, height, width){}
		cupboard(cupboard &c):Tree(c), Door(c){};
		
		int TO_GET_AGE(){
			return Tree::age;
		}
		string TO_GET_MODEL(){
			return Door::model;
		}
		

		void TO_SHOW(){
			Tree::TO_SHOW();
			Door::TO_SHOW2();
		}
};


int main(){
	Door d("AMI Mebel", 200, 100);
	d.TO_SHOW2();
	Tree t("birch", 2, 30);
	t.TO_SHOW();
	cupboard cupboard1("Oak", 2, 47, 50, 50, "CF");
	cupboard1.TO_SHOW();
}