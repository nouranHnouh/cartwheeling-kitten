#table the represent number and its occurance

# The output should look like this neatly formatted table:
"""
number | occurrence
     0 | 1
     1 | 2
     2 | 3
     3 | 2
     4 | 2
     5 | 1
     6 | 1
     7 | 2
     8 | 3
     9 | 1
    10 | 2
"""


import random

# Create random list of integers using while loop --------------------
random_list = []
list_length = 20
#add random number to the list 
while len(random_list) < list_length:
    random_list.append(random.randint(0,10))

# Aggregate the data -------------------------------------------------
count_list = [0] * 11 #create list of zeros
index = 0

while index < len(random_list):
    number = random_list[index]
    count_list[number] = count_list[number] + 1
    index = index + 1
    
# Write code here to summarize count_list and print a neatly formatted table that looks
# like this:

"""
number | occurrence
     0 | 1
     1 | 2
     2 | 3
     3 | 2
     4 | 2
     5 | 1
     6 | 1
     7 | 2
     8 | 3
     9 | 1
    10 | 2
"""

#print the table 
index=0
print "number|occurance"
num_len=len("number")

while index<len(count_list):
    num_spaces=num_len-len(str(index)) # calculate the number of spaces that each number takes
    
    #print " "*num_spaces+str(index)+'|'+(count_list[index])*"*" #print histogram table below
    print " "*num_spaces+str(index)+'|'+str(count_list[index])
    index+=1

#histogram
"""
number | occurrence
     0 | *
     1 | **
     2 | ***
     3 | **
     4 | **
     5 | *
     6 | *
     7 | **
     8 | ***
     9 | *
    10 | **
"""

