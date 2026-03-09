#include <iostream>

using namespace std;


int main(int argc, char* argv[]){


    char ch = 'a';

    cout << ch << " = " << +ch << endl;


    char ch_2 = 106;

    cout << ch_2 << " = " << +ch_2 << endl;

    // string name;
    // cout << "Enter your name: ";
    // cin >> name;
    // cout << "Hi " << name << endl;

    string full_name;

    cout << "Enter you full name: ";
    getline(cin, full_name);
    cout << "Hello, " << full_name << endl;

    return 0;
}