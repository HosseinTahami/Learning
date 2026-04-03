#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;


/*

    auto lambda_function_name = [](){};

    auto lambda_name = [The Variables it can Access outside it's Scope](Parameter){

        // BODY OF THE FUNCTION
    }
*/

int main(int argc, char* argv[]){

    auto say_hello = [](){
        cout << "Hello, World!\n";
    };

    say_hello();

// ===============================

        int multiplier = 3;

        auto multiply = [&multiplier](int num){

            multiplier++;
            cout << num * multiplier << endl;
            
        };

    multiply(5);

// ==========================

    vector<int> vecy = {5, 6, 1, 4, 2, 8, 7, 3};

    sort(vecy.begin(), vecy.end(), [](int n1, int n2){
        return n1 > n2;
        }
    );

    // sort(vecy.begin(), vecy.end());

    for_each(vecy.begin(), vecy.end(), [](int n1){
        cout << n1 << endl;
        }
    );

}

