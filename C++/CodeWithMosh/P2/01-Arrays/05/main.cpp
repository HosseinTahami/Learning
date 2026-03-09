#include <iostream>


using namespace std;

void printNumbers(int numbers[], int size){

    for (int i=0; i < size; i++){
        cout << numbers[i] << endl;
    }
}


int main(int argc, char* argv[]){

    int numbers[5] = {10, 30, 2, 23, 25};

    printNumbers(numbers, size(numbers));
    

    return 0;
}