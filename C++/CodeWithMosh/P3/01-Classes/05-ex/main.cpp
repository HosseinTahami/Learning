#include <iostream>
#include "TextBox.h"

using namespace std;



int main(){

    TextBox box;

    box.setValue("Hello Mother Fuckers !");
    cout << box.getValue() << endl;
    return 0;
}