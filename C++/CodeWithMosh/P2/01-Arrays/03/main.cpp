#include <iostream>


using namespace std;

int main(int argc, char* argv[]){

    int numbers[5] = {10, 30, 2, 23, 25};

    int otherNumbers[size(numbers)];

    for (int i; i < size(numbers); i++){
        otherNumbers[i]  = numbers[i];
    }



    return 0;
}