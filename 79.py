num1=int(input("Enter frist number"))
num2=int(input("Enter second number"))
squ=0
product=num1*num2
for x in range(max(num1,num2)+1):
	k=x*x
	if k==product:
		squ=1
if (squ==0):
	print("NO")
else:
	print("Yes")
