#include <iostream>
#include <limits>

using namespace std;

int main(int argc, char* argv[]){

    const int x = 10;

    // This is pointer of a constant operator
    // I can't change x, but I can change ptr 
    // to point to any other variable
    const int* ptr = &x;


    int y = 10;

    // This is a constant pointer
    // it only can point to one variable 
    // and can not be changed.
    int* const pointer = &y;

    return 0;
}