
from operator import itemgetter, attrgetter
"""You are required to write a program to sort the (name, age, height) tuples by ascending order where name is string, age and height are numbers. The tuples are input by console. The sort criteria is:
1: Sort based on name;
2: Then sort based on age;
3: Then sort by score.
The priority is that name > age > score."""

l=[]
while True:
	user_input=input(" ")
	if not user_input or user_input=="exit":
		break
	else:
		#create tuple of inpute and add them to list l
		l.append(tuple(user_input.split(",")))
#print (l) 
print (sorted(l,key=itemgetter(0,1,2))) 

