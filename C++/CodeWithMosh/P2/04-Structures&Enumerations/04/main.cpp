#include <iostream>
#include <vector>

using namespace std;


struct Date {

    short year = 1990;
    short month = 1;
    short day = 1;

};


struct Movie {
    string title;
    Date releaseDate;
    bool isPopular;

};



int main(){

    // Movie movie {
    //     "Term II",
    //     1990,
    //     4,
    //     5,
    //     false
    // };


    Movie movie {
        "Term II",
        {1990, 4, 5},
        false
    };

    cout << movie.releaseDate.year << endl;
    cout << movie.releaseDate.month << endl;
    cout << movie.releaseDate.day << endl;

    return 0;
}