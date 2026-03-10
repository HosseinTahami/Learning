#include <iostream>

using namespace std;



enum Action {

    List = 1,
    Add = 2,
    Update = 3,

};

/*

enum Action {

    List = 1,
    Add ,       // This will be 1+1 -> 2
    Update,    // This will be 1+2 -> 3

};


enum Action {

    List,   // This will be 0
    Add,    // This will be 0+1 -> 1
    Update  // This will be 0+2 -> 2

};

*/




int main(int argc, char* argv[]){

    int input;
    cout << "Enter 1-3: ";
    cin >> input;

    if (input == Action::List)
        cout << "Ciao !" << endl;

    return 0;
}