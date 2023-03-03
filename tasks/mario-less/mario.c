#include <cs50.h>
#include <stdio.h>

int main(void)
{

    int x, r, c, s;
    do
    {
        x = get_int("Height: ");
    }
    while (x < 1 || x > 8);             //Here checking inputs//

    for (r = 0; r < x; r++)             //creating rows//
    {
        for (s = 0; s < x - r - 1; s++) //height(x) - row(r) -1(last hash no need)//
        {
            printf(" ");
        }
        for (c = 0; c <= r; c++)  //Here printing until column(c) smaller than r(row)//
        {
            printf("#");
        }
        printf("\n");              // new line//
    }
}
