#include <iostream>
#include <vector>

using namespace std;

struct Movie {

    string title;
    int releaseYear;
    bool isPopular = false;
};


int main(){

    vector<Movie> movies;
    Movie m1 {"termin", 2390, true};
    Movie m2 {"fuck", 1290};
    Movie m3 {"safari", 1590, false};
    movies.push_back(m1);
    movies.push_back(m2);
    movies.push_back(Movie {"safari II", 1990, false});
    movies.push_back({"safari III", 1994, false});

    for (auto mov : movies){
        cout << mov.title << endl;
    }
    





    return 0;

}

