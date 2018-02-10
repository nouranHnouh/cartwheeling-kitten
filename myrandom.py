#create a list of numbers from 0 to 10, the length of the list is 20. 
#list with 20 randomly generated number
import random

random_list=[]
list_length=20
count=0
#create random numbers*2o times 
while count<list_length:
	random_list.append(random.randint(0,10))
	count+=1
print random_list

