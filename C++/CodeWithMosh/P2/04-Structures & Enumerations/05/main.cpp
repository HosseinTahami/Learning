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

    bool equals(const Movie& movie){
        return (title == movie.title &&
            releaseDate.year == movie.releaseDate.year &&
            releaseDate.day == movie.releaseDate.day &&
            releaseDate.month == movie.releaseDate.month &&
            isPopular == movie.isPopular
        );
    }

};



int main(){



    Movie movie1 {
        "Term II",
        {1990, 4, 5},
        false
    };

    Movie movie2 {
        "Term II",
        {1990, 4, 5},
        false
    };

    bool result = movie2.equals(movie1);

    cout << boolalpha << result << endl ;

    return 0;
}