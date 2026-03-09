#include <stdio.h>
#include <string.h>

char name[100];

char anotherName[100];

void gets(char* str);

int main(void) {
    printf("Enter Name: ");
    gets(name);
    puts(name);
    strcpy(anotherName, name);
    puts(anotherName);
    return 0;
}
