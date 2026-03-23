#include <iostream>
#include <map>
#include <string>

using namespace std;



int main(int argc, char* argv[]){


    map<string, int> people = {
        {"John", 43},
        {"Hossein", 44},
        {"Amir", 53}
    };

    cout << "John is " << people["John"] << " years old!" << endl;
    cout << "Hossein is " << people.at("Hossein") << " years old!" << endl;

    people["Marry"] = 12;
    people["Arian"] = 23;

    people.insert({"Mars", 89});
    people.insert({"Rosa", 13});

    people.erase("Hossein");

    // Elements in the map are sorted in ascending order by keys
    for (auto person : people){

        cout << person.first << "is fucking " << person.second << " years old" << "...\n";
    }

    map<string, int, greater<string>> revPeople = {{"Ali", 54}, {"Hossein", 52}, {"Akbar", 23}};

    for (auto person : revPeople){

        cout << person.first << " | " << person.second << endl;
    }

    return 0;
}
