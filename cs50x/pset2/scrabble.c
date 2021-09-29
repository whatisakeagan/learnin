#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

// Scrabble point array assigned to each letter of the alphabet
int POINTS[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};

int compute_score(string word);

int main(void)
{
    // Get input words from both players
    string word1 = get_string("Player 1: ");
    string word2 = get_string("Player 2: ");

    // Score both words
    int score1 = compute_score(word1);
    int score2 = compute_score(word2);
    
    //REMOVE LATER
    printf("%i\n", score1);
    printf("%i\n", score2);

    //Print the result (winner or tie)
    if (score1 > score2)
    {
        printf("Player 1 wins!\n");
    }
    else if (score1 < score2)
    {
        printf("Player 2 wins!\n");      
    }
    else
    {
        printf("Tie!\n");        
    }
}

int compute_score(string word)
{
    int score = 0;
    for (int i = 0, len = strlen(word); i < len; i++)
    {
        //Convert all letters to uppercase
        word[i] = toupper(word[i]);

        //Set value of the ith character
        if (isalpha(word[i]) == 0)
        {
            int j = 0;
        }
        else
        {
            //Use A as a the 0 index position by subtracting the ASCII value of A
            //The index value will correspond to the index in the array POINTS
            word[i] = word[i] - 65;
        }
        
        //Create integer j to store the value of the ith character without resetting index point
        int j = word[i];
        //Add value to score for each character in word
        score = score + POINTS[j];
    }
    //Return score (mostly because you can't NOT return something if what you're creating is non-void)
    return score;
}
