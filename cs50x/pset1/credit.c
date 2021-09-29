#include <stdio.h>
#include <cs50.h>
#include <math.h>
#include <stdlib.h>


int main(void)
{
    //Ask user for credit card number (get_long already rejects text)
    long ccnum = get_long("Credit card number: ");

    //Check length of input to make sure it's a possible cc
    //First, set ccnum to a separate variable to test length without changing ccnum
    long digitchk = ccnum;
    //Create a counting variable
    int i = 0;

    //Loop through ccnum (digitchk) by dividing by 10 to determine length
    while (digitchk > 0)
    {
        digitchk = digitchk / 10;
        i++;
    }

    //Check length (i == number of digits now) against acceptable lengths
    if (i == 13 || i == 15 || i == 16)
    {
        //Determine if valid according to Luhn's alg
        //Start w/ 2nd to last digit, multiply every other digit times 2. Then separate digits and
        // add together as though it was a string (only 2 possible digits at this step)
        int i1 = ((ccnum / 10) % 10) * 2;
        int i1A = i1 % 10;
        int i1B = (i1 / 10) % 10;
        int i2 = ((ccnum / 1000) % 10) * 2;
        int i2A = i2 % 10;
        int i2B = (i2 / 10) % 10;
        int i3 = ((ccnum / 100000) % 10) * 2;
        int i3A = i3 % 10;
        int i3B = (i3 / 10) % 10;
        int i4 = ((ccnum / 10000000) % 10) * 2;
        int i4A = i4 % 10;
        int i4B = (i4 / 10) % 10;
        int i5 = ((ccnum / 1000000000) % 10) * 2;
        int i5A = i5 % 10;
        int i5B = (i5 / 10) % 10;
        int i6 = ((ccnum / 100000000000) % 10) * 2;
        int i6A = i6 % 10;
        int i6B = (i6 / 10) % 10;
        int i7 = ((ccnum / 10000000000000) % 10) * 2;
        int i7A = i7 % 10;
        int i7B = (i7 / 10) % 10;
        int i8 = ((ccnum / 1000000000000000) % 10) * 2;
        int i8A = i8 % 10;
        int i8B = (i8 / 10) % 10;

        int luhnpt1 = i1A + i1B + i2A + i2B + i3A + i3B + i4A + i4B + i5A + i5B + i6A + i6B + i7A + i7B + i8A + i8B;

        //Sum the digits that weren't multiplied
        int luhnpt2 = ((ccnum % 10)
                       + ((ccnum / 100) % 10)
                       + ((ccnum / 10000) % 10)
                       + ((ccnum / 1000000) % 10)
                       + ((ccnum / 100000000) % 10)
                       + ((ccnum / 10000000000) % 10)
                       + ((ccnum / 1000000000000) % 10)
                       + ((ccnum / 100000000000000) % 10)
                      );

        //Add together
        int luhnTotal = luhnpt1 + luhnpt2;


        //IF the last digit == 0 (determined above), it's valid; proceed
        if ((luhnTotal % 10) == 0)
        {
            //Run 13 digit check -- VISA
            //All Visas start with 4
            if (i == 13)
            {
                if (((ccnum / 1000000000000) % 10) == 4)
                {
                    printf("VISA\n");
                }

                else
                {
                    printf("INVALID\n");
                }
            }

            //RUN 15 digit check -- AMEX
            //All American Express numbers start with 34 or 37
            if (i == 15)
            {
                if (((ccnum / 10000000000000) % 100) == 34 || ((ccnum / 10000000000000) % 100) == 37)
                {
                    printf("AMEX\n");
                }

                else
                {
                    printf("INVALID\n");
                }
            }

            //RUN 16 digit check -- MC or Visa
            //Visas start with 4
            //MasterCard numbers start with 51, 52, 53, 54, or 55
            if (i == 16)
            {
                if (((ccnum / 1000000000000000) % 10) == 4)
                {
                    printf("VISA\n");
                }

                else if (((ccnum / 100000000000000) % 100) == 51 || ((ccnum / 100000000000000) % 100) == 52
                         || ((ccnum / 100000000000000) % 100) == 53 || ((ccnum / 100000000000000) % 100) == 54 || ((ccnum / 100000000000000) % 100) == 55)
                {
                    printf("MASTERCARD\n");
                }

                else
                {
                    printf("INVALID\n");
                }
            }
        }
        else
        {
            printf("INVALID\n");
        }
    }

    //If NONE of the above work, print INVALID
    else
    {
        printf("INVALID\n");
    }
}
