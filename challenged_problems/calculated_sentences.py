"""Write a program that accepts a 
sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:"""

s=raw_input()
d={"DIGITS":0,"LETTERS":0}
for e in s:
	if e.isdigit():
		d["DIGITS"]+=1
	elif e.isalpha():
		d["LETTERS"]+=1
print ("LETTERS",d["LETTERS"])
print ("DIGITS",d["DIGITS"])
