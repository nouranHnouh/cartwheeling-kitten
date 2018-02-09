def list_less_ten(mylist):
	num=int(raw_input("Enter a number :"))
	new_list=[]
	for e in mylist:
		if e<num:
			new_list.append(e)
	return new_list
	
		

a=[1,1,2,3,5,8,13,21,34,55,89]
print list_less_ten(a)
