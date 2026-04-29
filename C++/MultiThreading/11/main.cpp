#include <iostream>
#include <thread>
#include <future>
#include <mutex>
#include <chrono>

using namespace std;


/* Async:

    This means without Synchronization
*/


int square(int x){
    return x*x;
}


int main(int argc, char* argv[]){

    future<int> asyncSquareFunction = async(&square, 12);

    for (int i=0; i < 10; i++){
        cout << square(i) << endl;
    }

    int result = asyncSquareFunction.get();

    cout << "Result is: " << result << endl;

    cout << endl;

    return 0;

}