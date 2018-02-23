


input_str=raw_input("Enter numbers ")

#create the dimenstions 
d=[int(x) for x in input_str.split(',')] 
#intialize row and colume 
row=d[0]
print (row) 
column=d[1]
print (column)

#intialize the array to zero 
multilist = [[0 for col in range(column)] for r in range(row)] 


#fill the array colume and row 
for r in range(row):
	for col in range(column):
		multilist[r][col]=r*col  
print(multilist)