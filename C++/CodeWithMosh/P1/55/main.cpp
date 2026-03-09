#include <iostream>

using namespace std;


void greet(string name){

    cout << "Hello, " << name << endl;

}

void greet(string title, string name){

    cout << "Hello, " << title << "." << name << endl;

}

int main(int argc, char* argv[]){

    greet("Hossein");
    greet("Mr", "Tahami");
    return 0;
}