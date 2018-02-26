a = int(input("enter the a value:"))
b = int(input("enter the b value:"))
print("\n Before swap ",(a, b))
a=a^b
b=a^b
a=a^b
print("\n After swaping ",(a, b))
