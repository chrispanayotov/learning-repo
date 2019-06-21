// Recreate the pyramids that Mario needs to jump over in the beginning of 
// World 1-1 in Super Mario Brothers

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int line;
    int height;

    // Pyramid height must be a positive int between 1 and 8

    while (true)
    {
        height = get_int("Please enter height between 1-8: ");
            if (height >= 1 && height <= 8)
            {
                break;
            }
    }
    for (line = 1; line <= height; line++)
    {
        int column;
        for (column = 0; column < height; column++)    // Left side of pyramid
        {
            if (column == (height - line)) 
            {
                for (column = (height - line); column < height; column++){
                    putchar('#');
                }
            }
            else 
            {
                printf(" ");
            }
        }
        printf("  ");
        for (column = 0; column < line; column++)    // Right side of pyramid
        {
            putchar('#');
        }
        printf("\n");
    }
}
