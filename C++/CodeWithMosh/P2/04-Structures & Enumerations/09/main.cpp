#include <iostream>

using namespace std;

struct Movie{

    string title;
    int year;


};


Movie getMovie(){
    return {"Terminator II", 1994};
}


void showMovie(Movie& movie){

    cout << movie.title << endl;
}


void showTitleOfMovie(Movie* movie){

    // cout << (*movie).title;
    cout << movie->title << endl;
}




int main(int argc, char* argv[]){


    auto movie = getMovie();
    showMovie(movie);

    showTitleOfMovie(&movie);

    return 0;
}