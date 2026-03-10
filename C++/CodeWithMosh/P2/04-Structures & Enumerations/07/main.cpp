#include <iostream>

using namespace std;


struct Point{

    int x;
    int y;
};


bool operator==(Point& first, Point& second){

    return(
        first.x == second.x && first.y == second.y
    );
};


ostream& operator<<(ostream& stream, Point& point){
    stream << "(" << point.x << ", " << point.y << ")" ;
    return stream;
}


int main(){

    Point p1, p2;

    p1 = {4, 5};
    p2 = {4, 3};

    cout << boolalpha << (p1 == p2) << endl;

    cout << p1 << endl << p2 << endl;
    return 0;
}