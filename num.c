#include<stdio.h>
void main()
{
int num,den;
long result=1;
printf("enter the den:");
scanf("%d",&den);
printf("enter the num:");
scnf("%d",&num);
while(num!=0)
{
result*=den;
--num;
}
printf("answer is=%d",result);
getch();
}
