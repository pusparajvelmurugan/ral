number=int(input("Enter the number:"))
c=''
while(number!=0):
	t=number%10
	if t%2!=0:
		c=c+' '+str(t)
	number=number//10
print("ODD number is",ans[::-1])
