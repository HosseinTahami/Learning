#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main(int argc, char* argv[]){

    fstream file;
    file.open("file.bin", ios::in | ios::out | ios::app | ios::binary);
    if (file.is_open()){
        file.close();
    }


    return 0;
}