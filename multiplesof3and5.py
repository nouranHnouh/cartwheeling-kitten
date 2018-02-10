#find the sum of all the multiple of 3 and 5 below 1000
sum_multiple=0
for number in range (1000):
	
	if number %3==0 or number%5==0:
		sum_multiple+=number
        
print sum_multiple
