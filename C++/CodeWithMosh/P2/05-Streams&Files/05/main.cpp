#include <iostream>
#include <fstream>
#include <string> // Good practice to include this explicitly

using namespace std;

class Movie {
    int id;
    string title;
    int year;

public: // Moved this UP so the constructor is public
    Movie(int id, string title, int year) {
        this->id = id;
        this->title = title;
        this->year = year;
    }

    void print() {
        // Added spaces around "in" and an endl for a clean new line
        cout << this->title << " in " << this->year << endl; 
    }
};

int main(int argc, char* argv[]) {

    ifstream file;
    file.open("data.csv");

    if (file.is_open()) {

        string str;
        // The safest loop: attempts to read the ID. 
        // If it hits the end of the file, the loop gracefully stops.
        getline(file, str);
        while (getline(file, str, ',')) {
            
            int id = stoi(str);
            
            getline(file, str, ',');
            string title = str;
            
            // Notice there is no ',' here! It stops at the end of the line.
            getline(file, str); 
            int year = stoi(str);
            
            Movie movie(id, title, year);
            movie.print();
        }
        file.close();
    }
    
    return 0;
}