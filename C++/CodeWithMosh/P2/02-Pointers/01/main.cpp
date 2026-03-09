#include <iostream>
#include <limits>

using namespace std;

int main(int argc, char* argv[]){

    int number = 10;
    cout << &number << endl;


    int* ptr_number = nullptr;

    ptr_number = &number;

    cout << ptr_number << endl;

    cout << *ptr_number << endl;

    return 0;
}