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

    // bool operator==(const Movie& movie) const {
    //     return (title == movie.title &&
    //         releaseDate.year == movie.releaseDate.year &&
    //         releaseDate.day == movie.releaseDate.day &&
    //         releaseDate.month == movie.releaseDate.month &&
    //         isPopular == movie.isPopular
    //     );
    // }

};

// C++ Operator Overloading !!

bool operator==(const Movie& first, const Movie& second) {
    return (first.title == second.title &&
        first.releaseDate.year == second.releaseDate.year &&
        first.releaseDate.day == second.releaseDate.day &&
        first.releaseDate.month == second.releaseDate.month &&
        first.isPopular == second.isPopular
    );
}

ostream& operator<<(ostream& stream, const Movie& movie){
    stream << '"'<<movie.title <<'"' << " in " << movie.releaseDate.year << endl;
    return stream;
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

    bool result = movie1 == movie2;


    cout << movie1;

    return 0;
}