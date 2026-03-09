#include <iostream>
#include <limits>

using namespace std;



int main(int argc, char* argv[]){

    int numbers[5] = {10, 30, 2, 23, 25};

    cout << sizeof(long long) << endl;
    cout << sizeof(size_t) << endl;
    
    cout << "MAX long long: " << numeric_limits<long long>::max() << endl;

    cout << "MIN long long: "<< numeric_limits<long long>::min() << endl;

    cout << "MAX size_t: " << numeric_limits<size_t>::max() << endl;
    cout << "Min size_t: " <<numeric_limits<size_t>::min() << endl;


    return 0;
}