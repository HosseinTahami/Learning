#include <iostream>
#include <limits>

using namespace std;


int main(int argc, char* argv[]){

    int numbers[] = {10, 20, 30};

    int* ptr = numbers;

    cout << &numbers << endl;

    cout << numbers << endl;

    cout << *numbers << endl;

    cout << *(numbers + 1) << endl;

    cout << *(numbers + 2) << endl;

    ptr = numbers;

    cout << ptr << endl;

    cout << *ptr << endl;

    cout << ptr[0] << endl;

    cout << ptr[1] << endl;

    cout << ptr[2] << endl;

    return 0;
}