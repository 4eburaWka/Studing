#include <iostream>

using std::cout; using std::string; using std::cin; using std::endl; 

//переменная числа рабочих на заводе 
const int am = 15;



//создадим функцию для генерации квалификации работников :
string getquality() {
  bool cond = false; 
  string result; 
  static int counter1 = 0 , counter2=0 , counter3 =0 , counter4 =0 ;
  string Qty[4] = { "high level worker", "average level worker", "low level worker","trainee" };
  do {
    int rnd = rand() % 4 + 1;
    cout << rnd<<" ";
    if (rnd == 1 && counter1 < 6) {
      result = Qty[0];
      counter1++;
      cond = true;
      return result;
      
    }


    if (rnd == 2 && counter2 < 2) {
      result = Qty[1];
      counter2++;
      cond = true;
      return result;
      
    }

    if (rnd == 3 && counter3 < 3) {
      result = Qty[2];
      counter3++;
      cond = true;
      return result;
      
    }

    if (rnd == 4 && counter4 < 4) {
      result = Qty[3];
      counter4++;
      cond = true;
      return result;
    }
  } while (cond==false);
}

//создадим функцию для генерации работоспособности в конкретный  для работников разных классов :
double getKpd(string quality) {
  double kpd = 0.0;
  if (quality.at(0) == 'h') {
    kpd = 6.0 * ((rand() % 3 + 2)/10.0);
    return kpd;
  }

  if (quality.at(0) == 'a') {
    kpd = 5.0 * ((rand() % 2 + 1) / 10.0);
    return kpd;
  }

  if (quality.at(0) == 'l') {
    kpd = 4.0 * ((rand() % 15 + 5) / 100.0);
    return kpd;
  }

  if (quality.at(0) == 't') {
    kpd = 5.0 * ((rand() % 2 + 1) / 100.0);
    return kpd;
  }

  return 1;
}


//создадим функцию для генерации случаных имени с фамилией:(+)
string getname() {
  //инициализация имён и фамилий  для идентификации агентов 
  string  names[14] = { "Anna","Dmitriy","Zhenya","Andrey","Nick","John","Ivan","Vanya","Danila","Denis","Denchik","Vova","Garik","Anton" };
  string surnames[12] = { "Kovalev","Yarmolenko","Syhoi","Dolgiy","Puchincky","Karagodin","Dubina","Yasuk","Novy","Star","Delphy","Lacarte" };
  int gN = rand() % 13 + 0;
  int gS = rand() % 11 + 0;
  string name = names[gN] + " " + surnames[gS];

  return name;
};


//создадим функцию инициализации работников(имени и квалификации) :
void set(string Names[],  const int am, string quality[])
{
  static int id = 0;
  for (int  i = 0; i < am ; i++)
  {
    id++;
    Names[i] = getname();
    quality[i] = getquality();

  }
}

// создадим функцию вывода информации о работниках завода :
void getinfo(string Names[], const int am, string quality[]) {
  static int id = 1;
  cout << "there is the entire stuff of emploee:  " << endl; 
  for (size_t i = 0; i < am; i++)
  {
    if (i == 0) {
      cout << "# " << "        " << "Full name:                              " << "Quality: \n\n";
    }
    cout << id << "            " << Names[i] << "                            " << quality[i] << endl;
    id++;
  }
}


// функция ,симулирующая условия работы :
void dowork(string Names[], const int am, string quality[]){
  static int simulation = 1;
   int day = 1;
  cout << "simulation " << simulation<<endl;
  simulation += 1;
  double progress = 0.0;
  
  do {
    double AMoP = day;
    if (progress >= 100) {
      cout << "on the day  " << day << "Work was finished " << endl;
      cout << "average volume of work done = " << progress /AMoP ;
    }
  
    
    for (int  i = 0; i < am; i++)
    {
      progress=progress + getKpd(quality[i]);
    }
    
    cout << "for the  day  "<< day << " crew has done " << progress << " % " << "of the all volume of work " << endl;
    day++;
  } while (progress < 100.0);

  
}



int dowork2(string Names[], const int am, string quality[]) {
  static int simulation = 1;
  int day = 1;
  cout << "simulation №  " << simulation << endl;
  simulation += 1;
  double progress = 0.0;

  do {
    double AMoP = day;
    if (progress >= 100) {
      cout << "on the day  " << day << "Work was finished " << endl;
      cout << "average volume of work done = " << progress / AMoP;
    }


    for (int i = 0; i < am; i++)
    {
      progress += getKpd(quality[i]);
    }
cout << "for the  day " << day << " has done " << progress << " % " << "of the all volume of work " << endl;
    day++;
  } while (progress < 100.0);

  return day-1;
}

int main() {
int temp = 0,Max=0,Min=100000000;
srand(time(NULL));
string Names[am];
double kpd1[am];
string quality[am];
int day = 0;
set(Names, am, quality);
getinfo(Names, am, quality);
double AMoD = 0.0;



cout << endl << endl;
//для первого задания :
cout << "task 1 :   " << endl<<endl<<endl;
dowork(Names, am, quality);

// Второе задание :

cout << "task 2 :   " << endl<<endl<<endl;
for (int i = 0; i < 100; i++)
{  
  temp=dowork2(Names, am, quality);
  AMoD += temp;
  
  // поиск минимального количества дней:
  if (temp < Min) { Min = temp; }
  //поиск максимального количества дней :
  if (temp > Max) { Max = temp; }
}
cout << "maximum amount of days required to complete this work -  " << Max<<endl;
cout << "minimum amount of days required to complete this work -  " << Min<<endl;
cout << "average amount of days require to complete this work - " << AMoD / 100.0;



  return 47;
}