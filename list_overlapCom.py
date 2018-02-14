#list overlap comprehension
#functiom list_overlap takes two list 
import random 
#and check for common elemets. 
#and return a list that has the common elements of two list
#without duplicate.
def list_overlap(listA,listB):
    overlap_list=[] # create new list 
    overlap_list=[e for e in set(listA) for i in set(listB) if e==i]
    
    return overlap_list
#define two list
a=random.sample(range(1,30),12)
#print a 
b=a=random.sample(range(1,30),16)
#print b
b =[1, 2, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 89]
#test the procedure 
print list_overlap(a,b)
