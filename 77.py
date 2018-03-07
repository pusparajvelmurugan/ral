num=int(input("Enter any number"))
ans=""
for i in range(1,num+1):
	if num%i==0:
		ans=ans+" "+str(i)
print(ans)
