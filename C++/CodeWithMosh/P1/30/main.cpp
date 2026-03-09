#include <iostream>
#include <limits>


using namespace std;

int main(int argc, char* argv[]){


    bool isNewUser = false;
    cout << "Is New User: " << isNewUser << endl;

    // boolalpha is sticky, so to remove it use noboolalpha

    cout << "Is New User: " << boolalpha << isNewUser << endl;

    return 0;
}