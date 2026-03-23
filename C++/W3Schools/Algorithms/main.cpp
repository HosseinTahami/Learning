#include <iostream>
#include <iomanip>
#include <algorithm>
#include <vector>
#include <set>
#include <string>

using namespace std;


int main(int argc, char* argv[]){

    vector<int> numbers = {7, 4, 1, 8, 9, 2, 11, 10};
    set<string> cars = {"Volvo", "BMW", "Mazda", "Benz", "Ford", "Ferrari"};

    sort(numbers.begin()+3, numbers.end());


    for (auto it=numbers.begin(); it != numbers.end(); it++){

        cout << *it << endl;
    }

    auto find_it = find(cars.begin(), cars.end(), "Ferrari");

    cout << find_it << " || " << *find_it << endl;

    return 0;
}