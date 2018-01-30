#string indexing 
word= 'assume'
print word[3]
print word [3:5] # starting from index position 3 and end at 5-1 
print word [3:6]
print word[4:] # print from 4 to the end ( to position 6-1)
print word [:2]# select from position 0 up to position 2 (2-1)
print word [:] # selecting form begining to the end 

# Python code that prints out Udacity (with a capital U), 
# given the definition of s below.

s = 'audacity'
print 'U'+s[2:8] 
print s[:-1] # give all character except for last one 
print s[:3]+s[3:] # give the whole character
#string indexing
t='Hi'
print t[:3]+t[3:]
