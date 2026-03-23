#include <iostream>
#include <vector>
#include <string>
#include <list>

using namespace std;

int main(int argc, char* argv[]){

    vector<string> cars = {
        "Mazda",
        "Volvo",
        "BMW",
    };

    list<string> listOfCars = {
        "Mazda",
        "Jeep",
        "BMW",
        "Benz",
        "Ferrari",
    };


    listOfCars.push_back("Fuck you !!");
    listOfCars.push_front("Fuck you infront of !!");

    cars.push_back("Tesla1");
    cars.push_back("Tesla2");
    cars.insert(cars.begin(), "Tesla");
    cars.pop_back();
    
    cars.front() = "V-Front";
    cars.back() = "V-back";
    
    for (string car : cars){
        cout << car << endl;
    }

    cout << "Front: " << cars.front() << " Back: " << cars.back() << endl;



    return 0;
}