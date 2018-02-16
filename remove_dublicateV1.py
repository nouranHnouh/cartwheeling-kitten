#function remove duplicate, take list as input and 
#remove the duplicate and store the elements in new list without duplicate
def remove_duplicate(mylist):
	newlist=[]
	
	for i in mylist:
		#if the element not in the list 
		if i not in newlist:
			#add it to the new list
			newlist.append(i)
	return newlist

a=[1,2,4,4,6,8,8,90,100]
print a
print remove_duplicate(a)



