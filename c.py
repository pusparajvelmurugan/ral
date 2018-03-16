num=int(input("enter any number"))
com=0
for i in range(1,num+1):
	if(num%i==0):
		com=com+1
if(com>2):
	print("yes")
else:
        print("no")
