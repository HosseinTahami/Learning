#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main(int argc, char* argv[]) {
    int numbers[3] = {1'000'000, 2'000'000, 3'000'000};

    ofstream file("numbers.bin", ios::binary);
    
    if (file.is_open()){
        file.write(reinterpret_cast<char*>(&numbers), sizeof(numbers));
        file.close();
    }
    return 0;
}