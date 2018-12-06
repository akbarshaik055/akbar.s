print("Enter '0' for exit.");
s= input("Enter any character: ");
if s == '0':
    exit();
else:
    if((s>='a' and s<='z') or (s>='A' and s<='Z')):
    	print(s, "is an alphabet.");
    else:
    	print(s, "is not an alphabet.");
