number=int(input("Enter any number"))
c=0
for x in range(1,num+1):
	if(number%x==0):
		c=c+1
if(c>2):
	print("composite")
else:
        print("Not composite")
