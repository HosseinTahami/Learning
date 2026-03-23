#include <iostream>
#include <list>
#include <string>
#include <iomanip>

using namespace std;

int main(int argc, char* argv[]){

    list<string> cars = {
        "Volvo",
        "BMW",
        "Tesla"
    };

    cout << "Front: " <<cars.front() << endl;
    cout << "Back: "<< cars.back() << endl;

    for (string car : cars){

        cout << car << endl;

    }

    cout << "Is the list Empty(): "<< boolalpha << cars.empty() << endl;



    return 0;
}