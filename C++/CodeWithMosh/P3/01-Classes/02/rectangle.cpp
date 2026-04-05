#include "rectangle.h"
#include <iostream>

using namespace std;

void Rectangle::draw(){

    cout << "Drawing a rectangle !" << endl;
    cout << "Dimensions: " << width << ", " << height << endl;
}


int Rectangle::getArea(){

    return width * height;
}