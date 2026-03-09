#include <stdio.h>

/*

int main(int argc, char* argv[]){

    printf("argc = %d\n", argc);

    for (int i=0; i < argc; i++)

    // *argv[i] = argv[i][0]

        printf("%d- %c\n", i, *argv[i]);
    return 0;
}


// ❯ ./ex04 hello goodbye well
// argc = 4
// 0- .
// 1- h
// 2- g
// 3- w


*/




int main(int argc, char* argv[]){

    printf("argc = %d\n", argc);

    for (int i=0; i < argc; i++)
        printf("%d- %s\n", i, argv[i]);
    return 0;
}

/*

❯ ./ex04 hello goodbye well
argc = 4
0- ./ex04
1- hello
2- goodbye
3- well

*/
