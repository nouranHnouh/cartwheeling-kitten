"""a program that accepts a comma separated 
sequence of words as input and prints the words 
in a comma-separated sequence after sorting them alphabetically.
"""

string=raw_input(" Enter string of word/s ").split(',')
items=[x for x in string]
items.sort()
print (items)

