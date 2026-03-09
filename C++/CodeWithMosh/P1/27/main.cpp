#include <iostream>
#include <cmath>
#include <cstdlib>
#include <ctime>


using namespace std;


int main(int argc, char* argv[]){
    

    long elapsedSeconds = time(nullptr);
    srand(elapsedSeconds);
    int number = rand() % 6 + 1;
        
    cout << number << endl;

    return 0;
}