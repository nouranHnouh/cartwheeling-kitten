#bigger is procedure that takes two number as input and return the larger number
#version 2
def bigger(a,b):
    result=0
    if a>b:
        result=a
        
    else:
        result=b

   
    return result
#biggest is procedure that takes three numbers as input and returns the largest number
def biggest(a,b,c):
	return bigger(bigger(a,b),c) # call bigger to return the largest number


print biggest(3, 6, 9)
#>>> 9

print biggest(6, 9, 3)
#>>> 9

print biggest(9, 3, 6)
#>>> 9

print biggest(3, 3, 9)
#>>> 9

print biggest(2, 2, 1) 
#>>> 2
