#include <iostream>

using namespace std;

int main(int argc, char* argv[]){

    int numbers[7] = {1, 4, 9, 2, 8};

    cout << *numbers << endl;
    cout << numbers[0] << endl;
    cout << numbers[1] << endl;
    cout << *(numbers+1) << endl;




    return 0;
}