#include <iostream>


using namespace std;

struct Movie{

    string title;
    int releaseYear;
    bool isPopular = false;
};

int main(){


    Movie movie = {"Terminator", 1943};
    // string title = movie.title;
    // int releaseYear = movie.releaseYear;
    // bool isPopular = movie.isPopular;


    auto [title, releaseYear, isPopular] = movie;
    return 0;
}