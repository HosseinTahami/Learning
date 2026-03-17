#include "rectangle.h"
#include <iostream>



using namespace std;

void Rectangle::draw(){

    cout << "Drawing a rectangle !" << endl;
    cout << "Dimensions: " << width << ", " << height << endl;
}


int Rectangle::getArea(){

    return this -> width * this -> height;
}

int Rectangle::getWidth(){
    return this -> width;
}

void Rectangle::setWidth(int width){
    if (width < 0)
        throw invalid_argument("Width");
    this -> width = width;
}

int Rectangle::getHight(){
    return this -> height;
}

void Rectangle::setHight(int height){

    this->height = height;
}


/* Constructor  */
Rectangle::Rectangle(int width, int height){
    cout << "Constructing a Rectangle." << endl;
    setWidth(width);
    setHight(height);
}


/* Member initializer List */
// Rectangle::Rectangle(int width, int height): width{width}, height{height} {
// }

