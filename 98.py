n=int(input("Enter n number:"))
print("Enter ascending order:")
a=[]
for x in range(n):
	k=int(input())
	a.append(k)
	for x in range(n-1):
	  for y in range(x,n):
		if(a[x]>a[y]):
			ans=x+1
print(ans)
