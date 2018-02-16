#program that takes a list of numbers
#and makes new list of only first and last elemnts of given list
#list_end take a list as input and returns a new list 
#that has the first and last elements 
import random 
def list_end(mylist):
	newlist=[]
	newlist.append(mylist[0])
	newlist.append(mylist[-1])
	

	return newlist

a=[1,2,3,7,9,3,4]
print list_end(a) 
