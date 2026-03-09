#include <iostream>
#include <memory>


using namespace std;


int main(){

    unique_ptr<int> x(new int);

    *x = 10;

    return 0;
}