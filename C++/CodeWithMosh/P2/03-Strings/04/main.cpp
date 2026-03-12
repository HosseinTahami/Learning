#include <iostream>

using namespace std;

int main(){


    string name = "Hossein";
    cout << name.find('A') << endl;

    if (name.find('A') == -1){
        cout << "Does not exist !" << endl;
    }

    cout << name.find('s') << endl;
    cout << name.rfind('s') << endl;

    cout << name.find_first_of("sli") << endl;
    cout << name.find_first_not_of("H soli") << endl;
    cout << name.find_last_not_of("H soli") << endl;

    return 0;
}