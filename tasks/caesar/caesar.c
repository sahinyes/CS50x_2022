#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>


int main(int argc, string argv[])
{
    if (argc != 2) //There can be max 1 argument
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }

    for (int i = 0; i < strlen(argv[1]); i++)
    {
        if (!isdigit(argv[1][i])) // Getting key and checking if its digit or not
        {
            printf("Usage: ./caesar key\n");
            return 1;
        }
    }

    int k = atoi(argv[1]);  //Converting argument to an int
    string plaintext = get_string("Plaintext: ");
    printf("Ciphertext: ");

    for (int d = 0; d < strlen(plaintext); d++) // Getting lenght of plaintext
    {
        if (isupper(plaintext[d]))
        {
            printf("%c", (plaintext[d] - 65 + k) % 26 + 65); //Converting upper chars to cipher
        }
        else if (islower(plaintext[d]))
        {
            printf("%c", (plaintext[d] - 97 + k) % 26 + 97); //Converting lower chars to cipher
        }
        else
        {
            printf("%c", plaintext[d]);
        }
    }
    printf("\n");
}