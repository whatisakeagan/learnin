#include <cs50.h>
#include <stdio.h>

int main(void)
{
    //Prompt for start size
    int start;
    do
    {
        start = get_int("Start size: ");

    }
    while (start < 9);

    //Prompt for end size
    int end;
    do
    {
        end = get_int("End size: ");

    }
    //Make sure resulting population is greater than the starting
    while (end < start);

    //Calculate number of years until we reach threshold
    //Start "years" from scratch
    int years = 0;
    //Only run this loop until we reach the goal population
    while (start < end)
    {
        //iterate the year and its corresponding start population
        start = start + (start / 3) - (start / 4);
        years++;
    }

    //Print number of years
    printf("Years: %i\n", years);
}
