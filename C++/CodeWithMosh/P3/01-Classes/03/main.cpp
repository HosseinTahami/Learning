#include <iostream>
#include "Rectangle.h"

using namespace std;


int main(){

    Rectangle myRectangle;

    myRectangle.width = 10;
    myRectangle.height = 20;

    cout << "Rectangle Area: " << myRectangle.getArea() << endl;
}