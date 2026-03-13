#include <iostream>
#include <sstream>
#include <iomanip>

using namespace std;

string double_to_string(double num, int precision){

    stringstream stream;
    stream << fixed << setprecision(precision) << num;
    string str = stream.str();
    return str;
}

int main(){

    double num = 12.45;
    
    // string str = to_string(num);
    string str = double_to_string(num, 1);
    cout << str << endl;
}