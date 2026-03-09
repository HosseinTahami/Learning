#include <iostream>

using namespace std;

// Function Declaration
// ProtoType
void greet(string name);


int main(int argc, char* argv[]){

    greet("Tahami");
    return 0;
}

// Function Definition
void greet(string name){

    cout << "Hello, " << name << endl;
}