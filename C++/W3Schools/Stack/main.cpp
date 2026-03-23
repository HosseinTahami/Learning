#include <iostream>
#include <iomanip>
#include <string>
#include <stack>

using namespace std;

int main(int argc, char* argv[]){



    stack<string> cars ;

    cars.push("Volvo");
    cars.push("BMW");
    cars.push("Ford");
    cars.push("Tesla");
    cars.push("Benz");
    cars.push("Mazda");


    cout << cars.top() << endl; // The Top one, is the last one we pushed, so "Mazda"

    cars.top() = "Pride";

    cars.pop() // This will remove the last element that was pushed to the stack

    


    return 0;
}