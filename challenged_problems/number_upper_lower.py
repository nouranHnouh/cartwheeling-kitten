"""Write a program that accepts a sentence and 
calculate the number of upper case letters and lower case letters.
Suppose the following input is supplied to the program:"""
s= raw_input()
upper_case=0
lower_case=0
for e in s:
	if e.isupper():
		upper_case+=1
	elif e.islower():
		lower_case+=1
print ("UPPER CASE %s" %upper_case)
print ("LOWER CASE %s" %lower_case)

