#include <iostream>
#include <deque>
#include <string>


using namespace std;


int main(int argc, char* argv[]){


    deque<string> cars = {"Volvo", "Benz", "Ford", "Ferrari"};


    cout << cars.at(3);
    cout << cars.at(8);

    for (string car : cars){

        cout << car << endl;
    }


    return 0;
}