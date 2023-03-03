#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for(int row = 0; row < height; row++)
    {
        for(int col = 0; col < width; col++)
        {
            int average = round((image[row][col].rgbtBlue + image[row][col].rgbtGreen + image[row][col].rgbtRed) / 3.00);

            image[row][col].rgbtBlue = average;
            image[row][col].rgbtRed = average;
            image[row][col].rgbtGreen = average;
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    for(int row = 0; row < height; row ++)
    {
        for(int col = 0; col < width; col++)
        {
            int sepiaRed = round(.393 * image[row][col].rgbtRed + .769 * image[row][col].rgbtGreen + .189 * image[row][col].rgbtBlue);
            int sepiaGreen = round(.349 * image[row][col].rgbtRed + .686 * image[row][col].rgbtGreen + .168 * image[row][col].rgbtBlue);
            int sepiaBlue = round(.272 * image[row][col].rgbtRed + .534 * image[row][col].rgbtGreen + .131 * image[row][col].rgbtBlue);

            image[row][col].rgbtBlue = (sepiaBlue > 255) ? 255 : sepiaBlue;
            image[row][col].rgbtRed = (sepiaRed > 255) ? 255 : sepiaRed;
            image[row][col].rgbtGreen = (sepiaGreen > 255) ? 255 : sepiaGreen;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE temp;
    for(int row = 0; row < height; row++)
    {
        for(int col = 0; col < width / 2; col++)
        {
            temp = image[row][col];
            image[row][col] = image[row][width - col - 1];
            image[row][width - col - 1] = temp;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE temp[height][width];

    for(int row = 0; row < height; row++)
    {
        for(int col = 0; col < width; col++)
        {
            int sumRed = 0;
            int sumGreen = 0;
            int sumBlue = 0;
            float count = 0.00;
            for(int i = -1; i < 2; i++)
            {
                for(int j = -1; j < 2; j++)
                {
                    if(row + i < 0 || row + i > height -1 || col + j < 0 || col + j > width -1)
                    {
                        continue;
                    }

                    sumRed += image[row + i][col + j].rgbtRed;
                    sumGreen += image[row + i][col + j].rgbtGreen;
                    sumBlue += image[row + i][col + j].rgbtBlue;

                    count++;
                }
            }

            temp[row][col].rgbtRed = round(sumRed/count);
            temp[row][col].rgbtGreen = round(sumGreen/count);
            temp[row][col].rgbtBlue = round(sumBlue/count);
        }
    }

    for(int i = 0; i < height; i++)
    {
        for(int j = 0; j < width; j++)
        {
            image[i][j].rgbtRed = temp[i][j].rgbtRed;
            image[i][j].rgbtGreen = temp[i][j].rgbtGreen;
            image[i][j].rgbtBlue = temp[i][j].rgbtBlue;
        }
    }

    return;
}
