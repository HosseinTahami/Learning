#include <iostream>
#include <vector>
#include <thread>
#include <mutex>

// using namespace std;

std::mutex gLock;
static int shared_value;

void shared_value_increment(){

    std::lock_guard<std::mutex> lockGuard(gLock);
    shared_value += 1;
}

int main(int argc, char* argv[]){


    vector<thread> threads;

    for (int i=0; i < 1000; i++){
        threads.push_back(thread(shared_value_increment));
    }

    for (int i=0; i < 1000; i++){
        threads[i].join();
    }

    cout << "Shared Value: " << shared_value << endl;
    return 0;
}