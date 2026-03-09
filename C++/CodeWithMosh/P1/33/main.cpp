#include <iostream>


using namespace std;


int main(int argc, char* argv[]){

    int x = 1;

    double y = 2.3;
    double z = x + y;

    cout << z << endl;

    // C Style Casting
    z = x + (int)y;

    // static Style Casting
    z = x + static_cast<int>(y);


    int a = 10;
    int b = 3;

    double c = static_cast<double>(a) / b;

    cout << c << endl;

    return 0;
}