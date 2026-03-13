#include <iostream>
#include <fstream>

using namespace std;


int main(int argc, char* argv[]){

    ifstream file("num.bin", ios::binary);
    
    if (file.is_open()){
        int num;
        while(file.read(reinterpret_cast<char*>(&num),sizeof(int)))
            cout << num << ", ";
        file.close();
    }

    return 0;
}