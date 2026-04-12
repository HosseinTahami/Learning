#include <iostream>
#include <vector>
#include <thread>
#include <mutex>

using namespace std;

mutex gLock;
static int shared_value = 0;

void shared_value_increment(){
    cout << "Ciao !!" << endl;
    gLock.lock();
        shared_value++;
    gLock.unlock();
}

int main(int argc, char* argv[]){


    vector<thread> threads;

    for (int i=0; i < 1000; i++){

        threads.push_back(thread(shared_value_increment));
    }

    for (int i=0; i < 1000; i++){
        threads[i].join();
    }


    cout << "shared value: " << shared_value << endl;

    return 0;
}

