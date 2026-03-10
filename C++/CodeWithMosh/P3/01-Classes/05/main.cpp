#include <iostream>
#include "rectangle.h"

using namespace std;


int main(){

    Rectangle rectangle;

    rectangle.setWidth(10);
    rectangle.setHight(23);

    cout << "Rectangle Area: " << rectangle.getArea() << endl;
}