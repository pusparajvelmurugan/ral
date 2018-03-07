string=input("Enter the string:")
l=len(string)
string1=list(string)
k=round(l//2)
string1[k]='*'
ans=''
for x in string1:
	ans=ans+x
print(ans)
