#include <iostream>
#include <vector>
#include <thread>
#include <mutex>

using namespace std;

mutex gLock;
static int shared_value;

void shared_value_increment(){
    /*
    
    `lock_guard<mutex> lockGuard(gLock)` you are doing two things:

        1. Hiring the security guard (creating the lockGuard object).

        2. Handing them the specific padlock (gLock) and saying,
           "This is the lock you are in charge of."
    */
    lock_guard<mutex> lockGuard(gLock);
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