num=input("Enter a string")
list1=[]
list2=[]
for i in range(len(num)):
    if i%2==0:list1.append(num[i])
    else:list2.append(num[i])
print(" ".join(str(x) for x in list1),"".join(str(x) for x in list2))
