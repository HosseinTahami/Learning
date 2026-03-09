#include <stdio.h>

int main(int argc, char* argv[]){

    int* p; 
    int a = 5;
    p = &a;

    printf("%d\n", a);
    printf("%p\n", &a);
    printf("%p\n", p);
}

