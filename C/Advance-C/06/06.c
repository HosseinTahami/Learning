#include <stdio.h>


int main(int argc, char* argv[]){


    int* p;
    int var = 9;
    p = &var;

    printf("%p\n", p);
    printf("%p\n", &var);
    return 0;
}