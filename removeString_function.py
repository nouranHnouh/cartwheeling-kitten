#remove is function that remove sub from somestring 

def remove(somestring, sub):
    """Return somestring with sub removed."""
    location = somestring.find(sub) # find the location of sub 
    #print location #print sor testing only
    if location==-1: # if we cant find sub in somestring return somestring
        return somestring
    #otherwise, calculate the length of sub 
    length = len(sub)
    #print length

   #find the part before sub       
    part_before = somestring[:location]
    #print part_before
    #find the part after sub 
    part_after = somestring[location + length:]
    #print part_after
    #return somestring with sub removed 
    return part_before + part_after
       

# 
# test function 
print remove('audacitious', 'a') # remove a from "audacitious" and return "udacitious"
print remove('pythonic', 'ic') # remove ic from pythoinc and return python 
print remove('substring institution', 'string in')
print remove('ding', 'do')  # "do" isn't in "ding"; should print "ding"
print remove('doomy', 'dooming')  # and this should print "doomy"
