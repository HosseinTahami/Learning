#include <iostream>
#include <thread>
#include <condition_variable>
#include <mutex>

using namespace std;

mutex gLock;
condition_variable cv;
int result = 0;
bool isReady = false;


void reporter(){

    gLock.lock();
    if (!isReady){
        cv.wait(gLock);
    }
    cout << "Report is ready: " << endl;
    cout << "Resutl = " << result << endl;
    gLock.unlock();
}

void worker(){

    cout << "Start Working..." << endl;
    gLock.lock();
    result += 10;
    result += 1;
    result += 16;
    isReady = true;
    cout << "Work is done !" << endl;
    gLock.unlock();
    cv.notify_one();
}


int main(int argc, char* argv[]){

    thread working_thread(worker);
    thread reporting_thread(reporter);

    working_thread.join();
    reporting_thread.join();

    return 0;
}
