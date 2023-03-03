#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

typedef uint8_t BYTE;
#define BLOCK_SIZE 512
#define FILE_SIZE 8


int main(int argc, char *argv[])
{
    // Checking input
    if (argc!=2)
    {
        printf("Usage: ./recover image \n");
        return 1;
    }

    // Open file and checking
    FILE *rfile = fopen(argv[1], "r");
    if (rfile == NULL)
    {
        printf("Cannot open the file \n");
        return 1;
    }

    unsigned char buffer[BLOCK_SIZE];
    int counter = 0;
    FILE *wfile = NULL;
    char filename [8];

    while (fread(buffer, sizeof(BYTE), BLOCK_SIZE, rfile) == BLOCK_SIZE)
    {
        // Controlling bytes if starts with jpeg or not
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            //Will start with here to create
            if (counter == 0)
            {
                sprintf(filename, "%03i.jpg", counter);
                wfile = fopen(filename, "w");
                fwrite(buffer, sizeof(BYTE), BLOCK_SIZE, wfile);
                counter++;
            }
            //Will close file and will write to in a new file
            else
            {
                fclose(wfile);
                sprintf(filename, "%03i.jpg", counter);
                wfile = fopen(filename, "w");
                fwrite(buffer, sizeof(BYTE), BLOCK_SIZE, wfile);
                counter++;
            }
        }

        else if (counter != 0)
        {
            fwrite(buffer, sizeof(char), BLOCK_SIZE, wfile);
        }

    }
    fclose(wfile);
    fclose(rfile);
}