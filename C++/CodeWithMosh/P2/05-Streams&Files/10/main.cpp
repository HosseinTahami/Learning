#include <iostream>
#include <sstream>
#include <string>

using namespace std;


int main(int argc, char* argv[]){

    string str = "10 40";
    stringstream stream;
    stream.str(str);

    int first , second;

    stream >> first; 
    stream >> second;
    cout << first + second << endl;
}