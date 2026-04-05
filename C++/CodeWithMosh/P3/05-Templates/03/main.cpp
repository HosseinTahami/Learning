#include <iostream>

using namespace std;

// int larger(int first, int second){
//     return (first > second ) ? first : second;
// }

// Generic Programming
template<typename T>
T larger(T first, T second){
    return (first > second ) ? first : second;
}

int main(int argc, char* argv[]){

    cout << larger(1.1, 2.2) << endl;
    cout << larger<double> (1.4, 5) << endl;
    cout << larger<double> (1.4, 1) << endl;
    return 0;

}