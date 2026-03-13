#include <iostream>
#include <sstream>

using namespace std;

struct Movie{

    string title;
    int year;

};


Movie parse_movie(string input){


    stringstream stream(input);
    Movie movie;

    getline(stream, movie.title, ',');
    stream >> movie.year;

    return movie;


}

int main(int argc, char* argv[]){


    auto movie = parse_movie("Avengers II, 2019");

    cout << movie.title << " by " << movie.year << endl;

    return 0;
}