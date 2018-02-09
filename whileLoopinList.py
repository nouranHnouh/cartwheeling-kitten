# Let's learn a little bit of Data Analysis and how we can use
# loops and lists to create, aggregate, and summarize data

# For the part 1, we'll learn a basic way of creating data using
# Python's random number generator.

# To create a random integer from 0 to 10, we first import the 
# "random" module

import random

# We then print a random integer using the random.randint(start, end) function
print "Random number generated: " + str(random.randint(0,10))

# We now want to create a list filled with random numbers. The list should be 
# of length 20

random_list = [] #empty list 
list_length = 20

# a while loop that populate this list of random integers. 
count=0
while count<list_length:
    random_list.append(random.randint(0,10))
    count+=1
    
# When we print this list, we should get a list of random integers such as:
# [7, 5, 1, 6, 4, 1, 0, 6, 6, 8, 1, 1, 2, 7, 5, 10, 7, 8, 1, 3]
print random_list