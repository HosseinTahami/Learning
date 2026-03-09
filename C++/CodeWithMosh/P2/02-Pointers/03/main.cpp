#include <iostream>
#include <limits>

using namespace std;

// void increasePrice(float& price){

//     price *= 1.2;
// }

void increasePrice(float* price){

    *price *= 1.2;
}

int main(int argc, char* argv[]){

    float price = 100;
    increasePrice(&price);
    cout << "New Price: " << price << endl;

    return 0;
}