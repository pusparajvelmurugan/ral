#include <stdio.h>
#include <math.h>
 
void main()
{
     int a,b,c,d,e;
     int sum = 0;
 
     printf("Enter the first term value of the A.P. series: ");
     scanf("%d", &a);
     printf("Enter the total numbers in the A.P. series: ");
     scanf("%d", &b);
     printf("Enter the common difference of A.P. series: ");
     scanf("%d", &c);
     sum = (n * (2 * a + (b - 1)* c ))/ 2;
     tn = a + (n - 1) * d;
     printf("Sum of the A.P series is: ");
     for (i = a; i <= tb; i = i + c )
     {
          if (i != tb)
               printf("%d + ", i);
          else
               printf("%d = %d ", i, sum);
     }
     getch();
}
