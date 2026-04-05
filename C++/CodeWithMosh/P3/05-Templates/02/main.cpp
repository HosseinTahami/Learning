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
    return 0;

}