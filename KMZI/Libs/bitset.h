template <int size=16>
class bitset{
public:
    bool set[size];
    bitset(){
        for (int i = 0; i < size; i++)
            this->set[i] = 0;
    }
    bitset(char symb){
        for (int i = size-1; i >= 0; i--)
            this->set[i] = (symb >> i) & 1; 
    }
    bitset(const bitset &obj){
        for (int i = 0; i < size; i++)
            this->set[i] = obj.set[i];
    }
    ~bitset(){}

    unsigned to_int(){
        unsigned num = 0;
        for (int i = size-1; i >= 0; i--)
            if (this->set[i]) 
                num |= (1 << i);
        return num;
    } 

    bool operator[](int i){
        return this->set[i];
    }
    bitset &operator=(const bitset &obj){
        for (int i = 0; i < size; i++)
            this->set[i] = obj.set[i];
        return *this;
    }
    bitset operator^(const bitset &obj){
        bitset temp;
        for (int i = 0; i < size; i++){
            temp.set[i] = this->set[i] ^ obj.set[i];
        }
        return temp;
    }
};