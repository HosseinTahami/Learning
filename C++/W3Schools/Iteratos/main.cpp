#include <iostream>
#include <iomanip>
#include <vector>
#include <algorithm>

using namespace std;

int main(int argc, char* argv[]){


    vector<string> cars = {
        "Volvo",
        "BMW",
        "Benz",
        "Fuck",
    };

    vector<string>::iterator it; // auto it;

    // .begin() The fucking first element of the data structure
    // .end() The fucking one element after the fucking last element of the data structure

    for (it=cars.begin(); it != cars.end(); it++){

        cout << *it << "\n";
    }

    vector<int> numbers = {1, 4, 5, 22, 12, 123, 4, 43, 2};


    sort(numbers.begin(), numbers.end());


    for (auto it=numbers.begin(); it != numbers.end(); it++){

        cout << *it << endl;
    }

    cout << "\n" << "==================" << "\n";

    for (auto it=numbers.rbegin(); it!=numbers.rend(); it++){
        cout << *it << endl;
    }



    return 0;
}