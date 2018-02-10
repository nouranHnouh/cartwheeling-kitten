#defining two list 
list1 = [1,2,3,4,5]
list2 = [1,2,3,4,5]
#proc function that take list as input and add to the list 
def proc(mylist):
    mylist = mylist + [6, 7]
#proc2 function take append to a list 
def proc2(mylist):
    mylist.append(6)
    mylist.append(7)

# print list1 and call proc function and pass list1 as its argument

print "demonstrating proc"
print list1
proc(list1)
print list1
print
#print list2 and call proc2 function and pass list2 as its argument
print "demonstrating proc2"
print list2
proc2(list2)
print list2

# add [6,7] to list3

list3 = [1,2,3,4,5]
list3 += [6, 7]

# procedure, proc3 that adds 6,7 to list3
def proc3(mylist):
    mylist+=[6,7]
print "demonstrating proc3"
print list3
proc3(list3)
print list3
