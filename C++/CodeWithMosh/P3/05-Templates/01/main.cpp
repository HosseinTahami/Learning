#include <iostream>

using namespace std;

template<typename T>
int larger(T first, T second){

    return (first > second) ? first : second;
}


int main(int argc, char* argv[]){


    cout << larger('a', 'b') << endl;
    return 0;
}

