#include <iostream>
#include <vector>
#include <thread>

using namespace std;


int main(int argc, char* argv[]){

    auto lambda = [](int x){

        cout << "Hello from thread #" << this_thread::get_id() << endl;
        cout << "Argument passed: " << x << endl;
    };

    vector<jthread> jThreads;

    for (int i=0; i < 10; i++){

        jThreads.push_back(jthread(lambda, i));
        
    }

    cout << "Hello from MAIN Thread !" << endl;

    return 0;
}
