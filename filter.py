#define funtion that determine if the value is even or not
#if it is even return true, otherwise return false
def iseven(num):
	if num%2==0:
		return True 
	else:
		return False
	
#use built-in function filter
#which return sequence of even number 
a=filter(iseven,[1,4,3,43,5,7,8,9,13,79])
print a 
