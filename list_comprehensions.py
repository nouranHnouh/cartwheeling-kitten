#python code that take a random list and print
#list that has even elements
#using list comprehension
import random 
numlist=[]
list_length=random.randint(5,15)
while len(numlist)<list_length:
	numlist.append(random.randint(1,75))
print numlist
even=[e for e in numlist if e%2==0]
print even

