#include <iostream>
#include "rectangle.h"

using namespace std;


int main(){

    Rectangle rec1(10, 29);
    Rectangle rec2{13, 43};



    cout << "Rectangle 1 Area: " << rec1.getArea() << endl;
    cout << "Rectangle 2 Area: " << rec2.getArea() << endl;
}