#include <stdio.h>


void swap(int num1, int num2){
    int tmp;

    tmp = num1;
    num1 = num2;
    num2 = tmp;
}


int main(int argc, char* argv[]){

    int num1 = 6;
    int num2 = 0;

    printf("Num 1, before swap = %d\n", num1);
    printf("Num 2, before swap = %d\n", num2);

    // Pass by Value
    swap(num1, num2);

    printf("Num 1, after swap = %d\n", num1);
    printf("Num 2, after swap = %d\n", num2);

    return 0;
} 