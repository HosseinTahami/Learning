#include <iostream>


using namespace std;

int main(int argc, char* argv[]){

    int numbers[5] = {10, 30, 2, 23, 25};

    // for (auto num : numbers){
    //     cout << num << endl;
    // }


    // for (int i=0; i < sizeof(numbers)/sizeof(int); i++){
    //     cout << numbers[i] << endl;
    // }

    for (int i=0; i < size(numbers); i++){
            cout << numbers[i] << endl;
    }

    return 0;

}