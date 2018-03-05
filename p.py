str = input("enter the str")
str = str
rev_str = reversed(str)
if list(str) == list(rev_str):
   print("It is palindrome")
else:
   print("It is not palindrome")
