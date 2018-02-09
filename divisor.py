

num=int(raw_input("Enter a number:"))#ask user for number
list_Range=list(range(1,num+1))#convert to list of number
divisor_List=[]#empty list 
#loop through list 
for e in list_Range:
	if num%e==0: 
		divisor_List.append(e) 
print divisor_List 
 