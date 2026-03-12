#include <iostream>

using namespace std;

int main(){

    // append()
    // erase(position, number)
    // clear()
    // replace(position, number, replacement)
    // insert(position, item)
    string name = "Hossein";
    name.append(" Tahami");
    name.insert(0, "Seyed ");
    cout << name << endl;

    name.erase(0, 6);
    cout << name << endl;

    name.replace(2, 2, "SS");
    cout << name << endl;


    name.clear();
    cout << name << endl;


    return 0;
}