
#function that print the sum of two variables 
def sum1 (a,b):
  a=a+b
  return a

print sum1 (2,123)

# # Define a procedure, abbaize, that takes
# two strings as its inputs, and returns
# a string that is the first input,
# followed by two repetitions of the second input,
# followed by the first input.
def abbaize(a,b):
  result=a+b*2+a
  return result








print abbaize('a','b')
#>>> 'abba'

print abbaize('dog','cat')
#>>> 'dogcatcatdog'
