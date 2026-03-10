#include <iostream>


using namespace std;


enum class Action{
    list = 1,
    del,
    update,
    add,
};


int main(){


    cout << "Enter 1-4: ";
    
    int input;
    cin >> input;

    if (input == static_cast<int>(Action::list))
        cout << "WTF !" << endl;

    return 0;
}