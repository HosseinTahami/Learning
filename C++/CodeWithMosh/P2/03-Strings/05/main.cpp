#include <iostream>

using namespace std;

int main(){


    string name = "Hossein Tahami";
    string copy = name.substr();
    cout << copy << endl;

    int slice = name.find(' ');

    string first_name = name.substr(0, slice);
    string last_name = name.substr(slice+1);

    cout << first_name << endl;
    cout << last_name << endl;

    

    return 0;
}