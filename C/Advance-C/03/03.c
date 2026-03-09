#include <stdio.h>

// 1. Change parameters to accept pointers (memory addresses)
void swap(int* num1, int* num2){
    int tmp;

    // 2. Use the '*' operator to get the actual values at those addresses
    tmp = *num1;
    *num1 = *num2;
    *num2 = tmp;
}

int main(int argc, char* argv[]){

    int num1 = 6;
    int num2 = 0;

    printf("Num 1, before swap = %d\n", num1);
    printf("Num 2, before swap = %d\n", num2);

    // 3. Pass the memory addresses of the variables using '&'
    swap(&num1, &num2);

    printf("Num 1, after swap = %d\n", num1);
    printf("Num 2, after swap = %d\n", num2);

    return 0;
}