#include <iostream>
#include "rectangle.h"

using namespace std;


int main(){

    Rectangle rectangle;

    rectangle.width = 10;
    rectangle.height = 20;

    cout << "Rectangle Area: " << rectangle.getArea() << endl;
}