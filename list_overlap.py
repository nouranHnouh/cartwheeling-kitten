#functiom list_overlap takes two list 

#and check for common elemets. 
#and return a list that has the common elements of two list
#without duplicate.
def list_overlap(listA,listB):
	overlap_list=[] # create new list 
	# go through list a element by element 
	for e in listA: 
		#go through list b elemnt by element
		for i in listB:
			#check if two elements are = and no duplicate
			if e==i and e not in overlap_list:
				#append the new list with the common elements 
				overlap_list.append(e)
	return overlap_list

#define two list
a=[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 89]
#test the procedure 
print list_overlap(a,b)
