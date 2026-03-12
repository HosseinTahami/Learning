#include <iostream>
#include <string>
#include <cstring>

using namespace std;

int main(){

    // Need "Null Terminator (\0)"
    char name[6] = {'S', 'h', 'a', 'd', 'i', '\0' };
    char myName[7] = "Givian";
    cout << "Name Length: " <<strlen(name) << endl;
    cout << "myName Length: " << strlen(myName) << endl ;

   
    strcat(name, myName);

    cout << name << endl;

    strcpy(name, myName);

    cout << strcmp(name, myName) << endl;

    cout << name << endl;

    return 0;
}
