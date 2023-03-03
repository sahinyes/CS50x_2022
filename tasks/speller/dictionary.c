// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <string.h>
#include <stdlib.h>
#include <stdio.h>
#include <strings.h>
#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// Variables
int word_count = 0;


// TODO: Choose number of buckets in hash table
const unsigned int N = 26;

// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO
    int hash_value = hash(word);
    node *cursor = table[hash_value];
    while (cursor != NULL)
    {
        if (strcasecmp(cursor->word, word) == 0)
        {
            return true;
        }
        cursor = cursor->next;
    }

    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    int total = 0;
    for (int i = 0; i < strlen(word); i++)
    {
        total += tolower(word[i]);
    }
    return total % N;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // TODO
    //Open Dictionary
    FILE *file = fopen(dictionary, "r");
    if (file == NULL)
    {
        printf("Cannot the file open");
        return false;
    }
    //Read words one at a time
    char word[LENGTH + 1];
    while (fscanf(file, "%s", word) != EOF)
    {
        //Create a new node
        node *temp = malloc(sizeof(node));
        if (temp == NULL)
        {
            return false;
        }

        // Getting Hash
        strcpy(temp->word, word);
        temp->next = NULL;
        int hash_value = hash(word);
        if(table[hash_value] == NULL)
        {
            table[hash_value] = temp;
        }
        else
        {
            temp->next = table[hash_value];
        }
        table[hash_value] = temp;
        word_count++;
    }

    fclose(file);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    return word_count;
}


void unnode(node *n)
{
    if(n->next != NULL)
    {
        unnode(n->next);
    }
    free(n);
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    for(int i = 0; i < N; i++)
    {
        if(table[i] != NULL)
        {
            unnode(table[i]);
        }
    }
    return true;
}