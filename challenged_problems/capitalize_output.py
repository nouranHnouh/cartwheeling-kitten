"""Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
Suppose the following input is supplied to the program:
"""
no_of_lines=2
lines=""
for x in range(no_of_lines):
	lines+=raw_input(" ")+"\n"
#print (lines)
print (lines.upper())

