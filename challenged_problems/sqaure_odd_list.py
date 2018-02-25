from math import sqrt
"""square only odd numbers in list"""
def square_odd(mylist):
	odd_number=[str(int(x)**2) for x in mylist if int(x)%2!=0] 
	return ",".join(odd_number)

#take the input from the user 
a=raw_input("Enter numbers ").split(',')
print (square_odd(a))