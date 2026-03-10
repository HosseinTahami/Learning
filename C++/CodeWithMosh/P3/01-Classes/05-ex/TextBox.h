#ifndef TEXT_BOX
#define TEXT_BOX


#include <iostream>

class TextBox{

    private:
    
        std::string value;
    
    public:
        std::string getValue();
        void setValue(std::string value);

};


#endif

