#include <stdio.h>

int main(void)
{
    char name = getline("What is your name: \n");
    printf("Hello, %s \n", name);
}