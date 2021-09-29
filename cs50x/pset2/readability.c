#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <math.h>

int count_letters(string usertext);
int count_words(string usertext);
int count_sentences(string usertext);

int main(void)
{
    // Get input text we want to assess
    string text = get_string("Text: ");

    //Print the number of characters
    int characters = strlen(text);

    //Print the number of letters
    int numletters = count_letters(text);

    //Print the number of words
    int numwords = count_words(text);

    //Print the number of sentences
    int numsentences = count_sentences(text);

    //Evaluate using Coleman-Liau index
    //index = 0.0588 * L - 0.296 * S - 15.8
    //L = average number of letters per 100 words in the text
    //S = average number of sentences per 100 words in the text
    float colemanliau = (0.0588 * (100 * numletters) / numwords) - (0.296 * (100 * numsentences) / numwords) - 15.8;
    int CL = round(colemanliau);
    
    //Print grade level
    //If < 1 or 16+ print special text
    if (CL < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (CL <= 16)
    {
        printf("Grade %i\n", CL);
    }
    else
    {
        printf("Grade 16+\n");
    }
}

//DEFINE COUNT_LETTERS
int count_letters(string usertext)
{
    int count = 0;
    for (int i = 0, len = strlen(usertext); i < len; i++)
    {
        int j = 0;
        if (isalpha(usertext[i]))
        {
            j = 1;
        }
        else
        {
            j = 0;
        }
        count = count + j;
    }

    return count;
}

//DEFINE COUNT WORDS
int count_words(string usertext)
{
    //Set initial word count to 1, because we're assuming (for the purpose of this exercise) that
    //the user entry will NOT end or begin with extraneous spaces
    int count = 1;
    //Each word is separated by a space
    //Words CAN include hyphens, but only one at a time (?)
    //Iterate over input, adding a +1 to count if we hit a space (?)
    //For the ith character of the input, check to see if it's a space, until we've gone through the whole thing
    for (int i = 0, len = strlen(usertext); i < len; i++)
    {
        int j = 0;
        if (usertext[i] == 32)
        {
            j = 1;
        }

        count = count + j;
    }

    return count;
}

//DEFINE COUNT SENTENCES
int count_sentences(string usertext)
{
    //Set initial word count to 0
    int count = 0;
    //For the purpose of this exercise, a sentence == a string that ends with a . ? or ! (though 
    //this would not be accurate in real world applications)
    //Iterate over input, adding a +1 to count if we hit a . or ? or !
    for (int i = 0, len = strlen(usertext); i < len; i++)
    {
        int j = 0;
        if (usertext[i] == 33 || usertext[i] == 46 || usertext[i] == 63)
        {
            j = 1;
        }

        count = count + j;
    }

    return count;
}
