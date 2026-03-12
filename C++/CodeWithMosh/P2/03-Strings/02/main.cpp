#include <iostream>
#include <string>

using namespace std;

int main(){

    string name = "Hossein Tahami";

    cout << *(&name) << endl;

    name[0] = 'h';

    cout << name << endl;


    cout << name.length() << endl;

    name += " is not ...";

    cout << name << endl;

    cout << name.starts_with('n') << endl;


}