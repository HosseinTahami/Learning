#include <iostream>

using namespace std;


struct Movie{

    string title;
    int year;
};



Movie getMovie(){
    return {"Ter II", 1034};
}

void showMovie(Movie& movie){
    cout << movie.title << endl;

}

int main(){


    auto movie = getMovie();
    showMovie(movie);
    return 0;
}