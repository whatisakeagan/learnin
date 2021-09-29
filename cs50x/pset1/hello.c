#include <stdio.h>
#include <cs50.h>

int main(void)
{
    //Prompt for person's name
    string name = get_string("What is your name?\n");
    //Say hello to them using their name
    printf("hello, %s\n", name);
}
