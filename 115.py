num=input("Enter your K1 and K2 value in single line with space:")
k1=int(num.split(" ")[0].strip())
k2=int(num.split(" ")[1].strip())
print("Enter your array:")
st=[]
for x in range(k1):
	a=int(input())
	st.append(a)
for x in range(k2-1):
	st.remove(min(st))
print("Ans is:",min(st))
