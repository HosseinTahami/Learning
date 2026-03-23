#include <iostream>
#include <iomanip>
#include <set>
#include <string>

using namespace std;

int main(int argc, char* argv[]){


    // By default, the elements in a set are sorted in ascending order. 

    set<string> cars = {"Volvo", "BMW", "Ford"};  

    set<int> numbers = {1, 25, 23, 5, 8, 7, 2, 6, 0, 23};

    // Reverse the Order
    set<int, greater<int>> revNum = {1, 25, 23, 5, 8, 7, 2, 6, 0, 23};


    for (int num : numbers){
        cout << num << "\n";
    }

    cout << "\n" << "================================" << "\n\n";

    for (int num : revNum){
        cout << num << "\n";
    }


    cars.insert("Pride");
    cars.insert("Audi");
    cars.erase("Volvo");

    cout << "\n" << "================================" << "\n\n";

    for (string car : cars){
        cout << car << "\n";
    }

    numbers.clear(); // Remove all the elements with the .clear()
    

    return 0;
}