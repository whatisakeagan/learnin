#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <math.h>
#include <stdlib.h>

//Declare functions for later
int validate_key(string key);
int encipher(string plaintext, string key);

//argc = number of command line arguments
//argv = array of strings representing all command line arguments provided
//argv[0] = name of program, so argc starts at 1
//argv[1] will be the key the user provides
int main(int argc, string argv[])
{
    //Make sure we've received a key
    if (argc == 1)
    {
        printf("ERROR: No key provided\n");
        return 1;
    }
    //Make sure we've only received ONE key
    else if (argc > 2)
    {
        printf("ERROR: Too many arguments provided\n");
        return 1;
    }
    //Key given; proceed
    else
    {
        //Validate key
        char key[30];
        //Copy the given string to key using strcopy so we don't permanently alter argv[1]
        strcpy(key, argv[1]);
        validate_key(key);

        //Get plaintext 
        string plain_text = get_string("plaintext: ");
        
        //Encipher and print plaintext
        encipher(plain_text, argv[1]);
        //DONE
        return 0;
    }
}

//DEFINE VALIDATION FUNCTION
int validate_key(string key)
{
    //Declare upper_key for use
    string upper_key = key;
    //Copy every character in key but uppercase
    for (int i = 0, len = strlen(key); i < len; i++)
    {
        upper_key[i] = toupper(key[i]);
    }
    //Validate key
    for (int i = 0, len = strlen(key); i < len; i++)
    {
        //Key must be 26 characters
        if (len < 26 || len > 26)
        {
            printf("ERROR: Key must contain 26 characters\n");
            exit(1);
        }
        //Key must be alphabetic
        if (isalpha(key[i]) == 0)
        {
            printf("ERROR: Not an alphabetic key\n");
            exit(1);
        }
    }
    //Key must not contain repeated letters
    //NOTE: this uses sequential pairwise comparisons, which isn't best
    //but was deemed accceptable for this assignment
    for (int i = 0; i < 26; i++)
    {
        for (int j = i + 1; j < 26; j++)
        {
            if (i != j)
            {
                if (key[i] == key[j])
                {
                    printf("ERROR: No duplicate characters\n");
                    exit(1);
                }
            }
        }
    }
    return 0;
}

//DEFINE ENCIPHER FUNCTION
int encipher(string plaintext, string key)
{
    int x = strlen(plaintext);
    char ciphertext[x + 1];
    for (int i = 0; i < x; i++)
    {
        //Because non-alpha chars are allowed in plaintext, 
        //still check if i is alpha
        if (isalpha(plaintext[i]))
        {
            //Preserve the case of plaintext, replace with cipher char
            if (islower(plaintext[i]))
            {
                ciphertext[i] = tolower(key[(int)plaintext[i] - 97]);
            }
            else if (isupper(plaintext[i]))
            {
                ciphertext[i] = toupper(key[(int)plaintext[i] - 65]);
            }
        }
        //If NOT alpha, don't change
        else
        {
            ciphertext[i] = plaintext[i];
        }
    }
    //Print ciphertext
    printf("ciphertext: %s\n", ciphertext);
    return 0;
}
