#include <iostream>
#include <iomanip>
#include <limits>

using namespace std;

int main( int argc, char* argv[]){

    cout << left << setw(10) << "Type" << setw(10) << "Size"  << endl
        << setw(10) << "int" << setw(15) << sizeof(int) << endl
        << setw(10) << "char" << setw(15) << sizeof(char) << endl;

    cout << "\n===================================\n" << endl;
    
    cout << numeric_limits<int>::min() << endl
        << numeric_limits<int>::max() << endl;

    return 0;
}