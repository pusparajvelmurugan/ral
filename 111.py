number=int(input("enter number:"))
count=0
while(number>0):
    count=count+1
    number=number//10
print("The number of digits in the number are:",count)
