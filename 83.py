num=input("Enter your seqence (Mod/Dividee):")
op=['%','/']
for x in num:
		if(x=='%'):
			k1=int(num.split(x)[0])
			k2=int(num.split(x)[1])
			ans=k1%k2
		elif(x=='/'):
			k1=int(num.split(x)[0])
			k2=int(num.split(x)[1])
			ans=k1//k2
print(ans)
