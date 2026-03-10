#include <iostream>

using namespace std;

struct Address{

    string street;
    string city;
    int zipCode;


};


struct Customer {

    int id = 0;
    string name;
    string email;
    Address address;

}

int main(){




    return 0;
}