#include <iostream>
#include <iomanip>

using namespace std;

int main(int argc, char* argv[]){


    // setw(n:) -> Set Width, Reserve number of characters
    // left -> left align, it is sticky, which means one time
    //          it is mentioned it will stay 
    cout << left << setw(10) <<"Spring" << setw(10) << "Nice" << endl 
        << setw(10) << "Summer" << setw(10) << "Hot" << endl;

    float num1 = 23.590234f;

    cout << setprecision(4) << num1 << endl;

    cout << "======================================" << endl;


    cout << left << setw(15) << "Course" << setw(10) << "Students" << endl
        << setw(15) << "C++" << setw(10) << 100 << endl
        << setw(15) << "JavaScript" << setw(10) << 430 << endl;

    return 0;
}