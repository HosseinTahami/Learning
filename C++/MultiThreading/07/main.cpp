#include <iostream>
#include <vector>
#include <atomic>
#include <thread>

using namespace std;

static atomic<int> shared_value = 0;

void increment_shared_value(){
    // ++, += Good
    shared_value++;
    //shared_value+=1;

    // Bad
    //shared_value = shared_value + 1;
}

int main(int argc, char* argv[]){

    vector<thread> threads; 
    
    for (int i=0; i < 1000; i++){

        threads.push_back(thread(increment_shared_value));
    }


    for (int i=0; i < 1000; i++){

        threads[i].join();
    }

    
    cout << "Shared Value: " << shared_value << endl;

    return 0;
}