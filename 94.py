num=(input("Enter N value:"))
k=int(input("Enter K value:"))
print("Enter the array values:")
a=[]
for x in range(0,num):
	t=int(input())
	a.append(t)
print(a[k-1])
