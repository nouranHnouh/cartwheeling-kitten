import random

#function element search take an ordered list and a number as input
#and search for that number in the list, the function decide 
#if the number is inside the list or not 
def element_search(mylist,number):
	newlist=sorted(mylist)
	print newlist 
	if number in newlist :
		return True
	else: 
		return False

#test the function 
a=random.sample(range(0,15),5)
#take a number from user to search 
number_search=int((raw_input("Please Enter a Number ?")))
print element_search(a,number_search)
