template<typename T>
class vector{
public:
    T arr[100]; int length = 0;
    vector(){}
    vector(int num){ length=num; }
    vector(int num, T el){
        for (int i = 0; i < num; i++)
            this->arr[length++] = el;
    }
    vector(vector<T> &vec, int beg, int count){
        for(int i = beg; i < beg+count; i++)
            this->arr[length++] = vec[i];
    }
    vector(int num, vector<T> el){
        for (int i = 0; i < num; i++)
            this->arr[length++] = el;
    }
    vector(const vector &obj){
        this->length = obj.length;
        for (int i = 0; i < obj.length; i++)
            this->arr[i] = obj.arr[i];
    }

    int size(){return length;}
    void push_back(T el){ this->arr[length++] = el; }
    void insert(vector<T> &vec2){
        for(int i = 0; i < vec2.length; i++)
            this->arr[length++] = vec2[i];
    }

    T* begin() { return arr; }
    T* end() { return arr + length; }

    T &operator[](int i){ return this->arr[i]; }
    T operator=(const T &obj){
        for (int i = 0; i < obj.length; i++)
            this->arr[i] = obj.arr[i];
        this->length = obj.length;
    }
};