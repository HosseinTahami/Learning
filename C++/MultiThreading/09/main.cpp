#include <iostream>
#include <thread>
#include <mutex>

using namespace std;

mutex gLock; //gLock: Global Lock

condition_variable gConditionVariable;

int main(int argc, char* argv[]){

    int result = 0;
    bool notified = false;

    // Reporting Thread
    // Wait on work, done by the working thread
    thread reporter([&](){

    });

    // Working Thread
    thread worker([&](){
        unique_lock<mutex> lock(gLock);
    });

    
    return 0;
}