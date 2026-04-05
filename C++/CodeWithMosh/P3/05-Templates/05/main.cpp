#include <iostream>

using namespace std;

template<typename K, typename V>
class Pair{

private:
    K key;
    V value;

public:
    // In-Line Constructor
    Pair(K key, V value) : key(key), value(value) {}
    
    template<typename K2, typename V2>
    friend ostream& operator<<(ostream& os, const Pair<K2, V2>& pair);
};

template<typename K, typename V>
ostream& operator<<(ostream& os, const Pair<K, V>& pair) {
    os << "[" << pair.key << ", " << pair.value << "]";
    return os;
}

int main(){

    Pair<int, string> myKeyValue(10, "Laptop");

    cout << myKeyValue << myKeyValue;
    
    return 0;
}