#include <iostream>
#include <limits>

using namespace std;


int main(int argc, char* argv[]){

    int numbers[] = {10, 20, 30};

    int* ptr = numbers;

    cout << *++ptr << endl;


    return 0;
}