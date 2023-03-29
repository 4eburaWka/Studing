#include <vector>
using namespace std;

class CongruentGen {
public:
    CongruentGen(vector<vector<unsigned long long>> &args, unsigned long long n){
        this->args = args;
        this->n = n;
    }

    unsigned long long gen() {
        if (t == args.size())
            t = 0;
        a = args[t][0];
        b = args[t++][1];
        x = (a * x + b) % n;
        return x;
    }

private:
    unsigned long long a;
    unsigned long long b;
    unsigned long long n;
    unsigned long long x = 1;
    unsigned t = 0;
    vector<vector<unsigned long long>> args;
};
