#include <iostream>
#include <thread>

using namespace std;

auto test(int x){
    cout << "Hello from thread !" << endl;
    cout << "Argument passed in: " << x << endl;
}

int main(int argc, char* argv[]){


    thread myThread(&test, 100);
    myThread.join();
    
    cout << "Hello From the MAIN Thread !" << endl;
    return 0;
}