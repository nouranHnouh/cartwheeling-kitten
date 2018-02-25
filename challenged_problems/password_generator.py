#this program takes passwords from user sperated with comma 
#and output valid password:
#valid password has these criteria:
#1. At least 1 letter between [a-z]
#2. At least 1 number between [0-9]
#1. At least 1 letter between [A-Z]
#3. At least 1 character from [$#@]
#4. Minimum length of transaction password: 6
#5. Maximum length of transaction password: 12
import re 

value=[]
input_password=input("Enter passwords: ")
#create list of input 
items=[i for i in input_password.split(',')]
for p in items:
	if len(p)<6 or len(p)>12:
		continue #move back to the loop
	else:
		pass 
	if not re.search ("[a-z]",p):
		continue
	elif not re.search("[0-9]",p):
		continue
	elif not re.search("[A-Z]",p):
		continue
	elif not re.search("[$#@]",p):
		continue
	elif re.search("\s",p):
		continue 
	else:
		pass
	value.append(p)
	print (",".join(value))


