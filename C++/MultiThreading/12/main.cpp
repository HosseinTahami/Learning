#include <iostream>
#include <thread>
#include <future>
#include <chrono>

using namespace std;

bool bufferedFileLoader(){

    size_t bytesLoaded = 0;
    while(bytesLoaded < 20000){
        cout << "thread: loading file..." << endl;
        this_thread::sleep_for(chrono::milliseconds(250));
        bytesLoaded += 1000;
    }

    return true;
}



int main (int argc, char* argv[]){


    future<bool> backGroundThread = async(
        launch::async,
        bufferedFileLoader
    );


    future_status status;

    // Our main program loop
    while(true){

        cout << "Main Thread is running... "<< endl;

        // artificial sleep 
        this_thread::sleep_for(chrono::milliseconds(50));

        status = backGroundThread.wait_for(chrono::milliseconds(1));

        if (status == future_status::ready){
            cout << "Our data is Ready...." ;
            cout << endl;
            break;
        }
    }


    return 0;
}