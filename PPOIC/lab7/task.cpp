#include <iostream>
using namespace std;

template <typename T, typename T1>
class Tree{
	public:
		T1 nameOfTree;
		T age, reliability;

		Tree(){
			nameOfTree = "";
			age = 0;
			reliability = 0;
		}
		Tree(T1 n, T a, T r){
			nameOfTree = n;
			age = a;
			reliability = r;
		}
		Tree(Tree &t){
			nameOfTree = t.nameOfTree;
			age = t.age;
			reliability = t.reliability;
		}

		void TO_SET(T a, T r, T1 n){
			age = a; reliability = r; nameOfTree = n;
		}

		T isReliable(){
			if(reliability > 50)
				return 0;
			return 1;
		}

		void TO_SHOW(){
			cout << "nameOfTree: " << nameOfTree << endl;
			cout << "age: " << age << "\nreliability: " << reliability << endl;
		}
};

template <typename T, typename T1>
class Door{
	public:
		T height, width; T1 model;
		Door(){
			model = "";
			height = 0;
			width = 0;
		}
		Door(T1 m, T h, T w){
			model = m;
			height = h;
			width = w;
		}
		Door(Door &d){
			this->model = d.model;
			this->height = d.height;
			this->width = d.width;
		}
		void TO_SET(T h, T w){
			height = h; width = w;
		}
		void TO_SET(T1 m){
			model = m;
		}

		void TO_SHOW(){
			cout << "Furniture: Door" << endl;
			cout << "Model: " << model << endl;
			cout << "Height: " << height << endl;
			cout << "Width: " << width << endl;
		}
};

template <typename T>
class SUM{
	private: 
		T a, b;
    public:
        SUM(){
            this->a = 0;
            this->b = 0;
        }
        SUM(T a, T b){
            this->a = a;
            this->b = b;
        }
        SUM(SUM &s){
            this->a = s.a;
            this->b = s.b;
        }
        T sum(T a)
            {return a;}
        
        T sum(T a, T b)
            {return a + b;}
        
        T sum(T a, T b, T c) {return a + b + c;}
};

int main(){
	Door<int, string> d("AMI Mebel", 200, 100);
	d.TO_SHOW();
	Tree<int, string> t("birch", 2, 30);
	t.TO_SHOW();
    SUM<int> qwer(1,1);
    cout << qwer.sum(1, 2, 3) << endl;
    cout << qwer.sum(1, 2) << endl;
    cout << qwer.sum(1) << endl;
}