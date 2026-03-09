#include <iostream>


using namespace std;


void greet(string name){

    cout << "Hello, " << name << endl;
}


string fullName(string firstName, string lastName){
    return firstName + " " + lastName;
}

int main(int argc, char* argv[]){



    // string myName = fullName("Hossein", "Tahami");

    // cout << myName << endl;

    greet(fullName("Hossein", "Tahami"));

}