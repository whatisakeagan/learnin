#include <cs50.h>
#include <stdio.h>

int main(void)
{
    //Prompt for desired height
    int height;
    do
    {
        height = get_int("Height: ");

    }
    //But make sure the user enters a value between 1 and 8
    while (height > 8 || height < 1);

    //As long as the width and row numbers are less than the height, print an incrementing number of #s
    for (int row = 0; row < height; row++)
    {
        for (int space = 1; space < (height - row); space++)
        {
            printf(" ");
        }

        for (int width = 0; width <= row; width++)
        {
            printf("#");
        }
        printf("\n");
    }
}
