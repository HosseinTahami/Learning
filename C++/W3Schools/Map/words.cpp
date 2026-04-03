#include <iostream>
#include <map>
#include <string>

using namespace std;

// Press "CTRL + D" to finish the fucking program.


int main(int argc, char* argv[]){

    map<string, size_t> word_count;
    string word;

    while(cin >> word)
        ++word_count[word];

    
    for (const auto w : word_count)
        cout << w.first << " occurs " << w.second << " time(s)." << endl;



    return 0;
}