#include <iostream>
#include <vector>
#include <thread>

using namespace std;

int main(){

    auto lambdaFunc = [](int x){

        cout << "Hello from thread #" << this_thread::get_id() << endl;
        cout << "Argument passed in: " << x << endl;
    };

    vector<thread> threads;

    for (int i=0; i < 10; i++){
        threads.push_back(thread(lambdaFunc, i+1));
        // threads[i].join();
    }

    for (int j=0; j < 10; j++){
        threads[j].join();
    }

    cout << "Hello From My Main THREAD !" << endl;
    return 0;
}