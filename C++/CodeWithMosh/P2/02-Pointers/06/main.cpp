#include <iostream>

using namespace std;

int main(){
    
    int numbers[] = {10, 20, 30};

    int* ptr = numbers + (size(numbers) - 1);


    for (int i=(size(numbers) - 1); i >= 0; i--){
        cout << numbers[i] << endl;
    }
    return 0;
}