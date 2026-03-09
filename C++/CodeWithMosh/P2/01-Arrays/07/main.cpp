#include <iostream>
#include <limits>

using namespace std;



int main(int argc, char* argv[]){

    int numbers[3] = {10, 30, 2};

    // manual unpacking
    // int x = numbers[0];
    // int y = numbers[1];
    // int z = numbers[2];


    auto [x, y, z] = numbers;

    cout << "X: "<< x << endl;
    cout << "Y: "<< y << endl;
    cout << "Z: "<< z << endl;

    return 0;
}