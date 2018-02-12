#include<stdio.h>
void main()
{
int num,den;
long result=1;
printf("enter the den:");
scanf("%d",&den);
printf("enter the num:");
scnf("%d",&num);
if(num!=0)
{
result*=den;
--num;
printf("yes",result);
  else
    printf("no",result);
getch();
}
