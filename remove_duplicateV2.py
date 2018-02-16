#function remove duplicate, take list as input and 
#remove the duplicate and store the elements in new list without duplicate
def remove_duplicate(mylist):
	#set function return a list with elements without duplicate
	newlist=list(set(mylist))
	return newlist 


a=[1,2,4,4,6,8,8,90,100]
print a
print remove_duplicate(a)
