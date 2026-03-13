#include <iostream>
#include <limits>

using namespace std;

int getNumber(string prompt){


    int num;
    
    while(true){
        cout << prompt << " : ";
        
        cin >> num;
        if (cin.fail()){
            cout << "Enter valid number!" << endl;
            cin.clear();
            cin.ignore(numeric_limits<streamsize>::max(), '\n');

        } else break;
    }

    return num;
    
}

int main(){
    

    int first = getNumber("First");
    int second = getNumber("Second");


    cout << "You entered " << first << " and " << second << endl;

    return 0;
}