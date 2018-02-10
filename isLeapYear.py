#procedure is_leap takes one input and return true if it is leap year
#otherwise, return false 
def is_leap(year):
    
    if year%4==0:
        leap=True
    if year%100==0:
    	leap=False
    if year %400==0:
    	leap=True
    else:
    	return False 
    return leap
#ask user for a year 
year=int(raw_input("Enter year :"))
print is_leap(year) # print whether the year is leap year or not 
