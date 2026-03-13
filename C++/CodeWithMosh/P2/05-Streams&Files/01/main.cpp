#include <iostream>
#include <limits>

using namespace std;


int main(){


    cout << "First: ";
    int first;
    cin >> first;
    /*  The function keeps throwing characters in the trash 
        until it either 
        - reaches the maximum count 
        - it finds and throws away the delimiter character
          whichever happens first.
     */
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    cout << "Second: ";
    int second;
    cin >> second;


    cout << "You entered " << first << " and " << second << endl;

    return 0;
}