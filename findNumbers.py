"""a program that find all such numbers wich are 
divisible by 7 but not multiple of 5
between 2000 and 3200 """
mylist=[]
for i in range(2000,3201):
	if i%7==0 and i%5!=0:
		mylist.append(i)
print mylist

