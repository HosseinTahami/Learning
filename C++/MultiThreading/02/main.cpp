#include <iostream>
#include <thread>

using namespace std;


int main(int argc, char* argv[]){

    auto myLambdaFunc = [](int x){
        
        cout << "Hello from thread !" << endl;
        cout << "argument passed in: " << x << endl;
    };

    thread myThread(myLambdaFunc, 100);
    myThread.join();

    cout << "Hello from my main Thread !" << endl;
    return 0;
}