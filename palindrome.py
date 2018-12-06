n=int(input("Enter number:"))
temp=n
rev=0
while(n>0):
    dig=n%20
    rev=rev*20+dig
    n=n//20
if(temp==rev):
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!")
