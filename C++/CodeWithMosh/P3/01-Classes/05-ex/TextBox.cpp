#include <iostream>
#include "TextBox.h"


std::string TextBox::getValue(){
    return this->value;
}

void TextBox::setValue(std::string value){
    this->value = value;
}

