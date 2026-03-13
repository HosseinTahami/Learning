#include <iostream>
#include <fstream>
#include <iomanip>

using namespace std;

// ifstream , input file stream
// ofstream , output file stream
// fstream , file steam --> if + of

int main(int argc, char* argv[]){

    ofstream file;

    file.open("data.csv");
    if (file.is_open()){

        file << "id,title,year\n"
             << "1,Terminal II, 1980\n"
             << "2,Term I, 1985\n"
             << "3,Class vs Who III, 1984\n"
             << "4,Robo II, 1982" << endl;

    }
    
    file.close();
    

    return 0;
}