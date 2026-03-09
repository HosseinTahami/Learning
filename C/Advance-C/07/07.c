#include <stdio.h>

int main(int argc, char* argv[]){

int a=4;
int* p;

p = &a;

printf("%d\n", a);

// Dereferencing
*p = 10;

printf("%d\n", a);

}