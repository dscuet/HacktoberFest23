// Structure can be defined as collection of dissimilar data members nder one name.

// // Example 1:
// #include<stdio.h>

// struct Rectangle
// {
//     int length;
//     int breadth;
// };

// int main()
// {
//     struct Rectangle r1;                 // r1 occupies 4 bytes
//     struct Rectangle r2 = {10,5};
//     r1.length = 15;
//     r1.breadth = 10;

//     printf("Area of rectangle r1 is : %d",(r1.length*r1.breadth));

//     return 0;
// }

// // Example 2: complex number

// struct Complex
// {
//     int real;
//     int img;
// };


// // Example 3:
// struct Student
// {
//     int roll;
//     char name[25];
//     char dept[10];
//     char address[50];
// };


// Example 4: Playing cards

#include<stdio.h>
struct Card
{
    int face;
    int shape;
    int color;
    char x;
};

int main()
{
    struct Card c;
    c.face = 1;
    c.shape = 0;
    c.color = 0;
    printf("\n%d",sizeof(c));
    // It takes 16 bytes instead of 13. This is because it is easier for our computer
    // to read 4 bytes at at a time. This is called padding.

    // struct Card deck[52];
    struct Card deck[52] = {{1,0,0},{2,0,0}};

    printf("\n%d",deck[0].face);
    printf("\n%d",deck[0].shape);
    printf("\n%d",deck[0].color);

    return 0;
}