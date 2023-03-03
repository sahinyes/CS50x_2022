#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <math.h>

char excl[] = {'.','!','?'};

int main(void)
{
    string text = get_string("Text: ");
    int letter = 0;
    int word = 1;
    int satz = 0;

    for (int i = 0; i < strlen(text); i++)
    {
        if (isalpha(text[i]))  // counting letters with isalpha
        {
            letter++;
        }
        else if (text[i] == ' ') // counting spaces
        {
            word++;
        }
        else if (text[i] == excl[0] || text[i] == excl[1] || text[i] == excl[2]) //I wanned try with array
        {
            satz++;
        }
    }

    float L = (float) letter / (float) word * 100;
    float S = (float) satz / (float) word * 100;

    int index = round(0.0588 * L - 0.296 * S - 15.8);  // Coleman-Liau index

    if (index < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (index > 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %i\n", index);
    }
}