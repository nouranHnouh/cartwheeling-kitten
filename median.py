# a procedure, median, that takes three
# numbers as its inputs, and returns the median
# of the three numbers.

# bigger procedure takes two inputs and return the bigger number

def bigger(a,b):
    if a > b:
        return a
    else:
        return b
#bigest procedure takes three inputs and return the biggest number 
def biggest(a,b,c):
    return bigger(a,bigger(b,c)) # calling bigger function

def median(a,b,c):
    big=biggest (a,b,c)
    if big==a:
        return bigger(b,c)
    elif big==b:
        return bigger(a,c)
    else:
        return bigger(a,b) 
        






print(median(1,2,3))
#>>> 2

print(median(9,3,6))
#>>> 6

print(median(7,8,7))
#>>> 7







