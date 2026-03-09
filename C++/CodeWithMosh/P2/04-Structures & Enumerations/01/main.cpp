#include <iostream>


using namespace std;
   

struct Movie{

    string title;
    int releaseYear;
};

struct Customer{
    int id;
    string name;
    string email;
};


int main(){

    // Movie movie;

    // movie.title = "Terminator";
    // movie.releaseYear = 2033;

    // cout << movie.title << endl;


    Customer customer;

    cout << "Enter your Name: ";
    getline(cin, customer.name);


    cout << "Enter your Email: ";
    getline(cin, customer.email);
  

    cout << "Name= " << customer.name << endl;
    cout << "Email=" << customer.email << endl;
    return 0;
}

// #include <iostream>

// using namespace std;

// int main() {
//     // --- Style Codes ---
//     const string RESET = "\033[0m";
//     const string BOLD = "\033[1m";
//     const string ITALIC = "\033[3m"; // Note: Some older terminals don't support italic
//     const string UNDERLINE = "\033[4m";

//     // --- Color Codes ---
//     const string RED = "\033[31m";
//     const string GREEN = "\033[32m";
//     const string BLUE = "\033[34m";
//     const string YELLOW = "\033[33m";

//     // --- Examples ---
    
//     // 1. Just Bold
//     cout << BOLD << "This text is BOLD." << RESET << endl;

//     // 2. Just Color
//     cout << GREEN << "Success! The operation worked." << RESET << endl;

//     // 3. Combining Styles (Color + Bold + Underline)
//     // You just chain the strings together before your text
//     cout << RED << BOLD << UNDERLINE << "ERROR: Critical failure!" << RESET << endl;

//     // 4. Italic
//     cout << ITALIC << BLUE << "This is some blue, italicized text." << RESET << endl;

//     // 5. Normal text to prove the reset worked
//     cout << "This is back to normal text." << endl;

//     return 0;
// }