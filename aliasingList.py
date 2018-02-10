#create spy list 
spy=[0,0,7]
#assign list to a variable
agent=spy
print spy # print spy list 
print agent # print agent list, it should be = to spy since it is pointing to the same list
#add 1 to 7 in agent list and save it in spy list 
spy[2]=agent[2]+1
#print new list
print spy 
print agent 
