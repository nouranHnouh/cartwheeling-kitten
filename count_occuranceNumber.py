# occurrences of the number 9 appear in our randomly made list
# 
#loop through the list and count the number of occurrences of the
# number 9.

import random

# 1. Create random list of integers using while loop
random_list = [] # empty list 
list_length = 20 
#loop when length of random_list is less than length of the list 
while len(random_list) < list_length:
  random_list.append(random.randint(0,10)) # append the list by random number from 0 to 10 
    
# loop through the list and count all occurrences
# of the number 9.
count=0
targetValue=0
while targetValue<len(random_list): 
    if random_list[targetValue]==9:
        count+=1
    targetValue+=1



# Test: If the `while` works
print random_list
print count
