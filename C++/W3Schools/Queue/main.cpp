#include <iostream>
#include <string>
#include <queue>



using namespace std;


int main(int argc, char* argv[]){


    queue<string> cars;

    cars.push("Volvo");
    cars.push("Ford");
    cars.push("Benz");
    cars.push("Mazda");


    cout << "Front: " << cars.front() << endl;

    cout << "Back: " << cars.back() << endl;



    return 0;
}