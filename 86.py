num=input("Enter any String:")
a=[]
flag=0
for x in num:
	if x not in a:
		a.append(x)
	else:
		flag=1
if(flag==1):
	print("No")
else:
	print("Yes")
