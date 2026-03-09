#include <iostream>


using namespace std;


void increasePrice(double& price){

    price*=1.2;
}


int main(int argc, char* argv[]){

    double price = 100;
    increasePrice(price);
    cout << price << endl;

    return 0;
}

// In C, using Pointers !


/*

// Using pointers to pass the exact memory address explicitly
void increasePrice(double* pricePtr) {
    *pricePtr *= 1.2; // Dereference the pointer to change the value
}

int main() {
    double price = 100;
    increasePrice(&price); // Explicitly pass the memory address of 'price'
    return 0;
}

*/