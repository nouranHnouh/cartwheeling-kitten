daysOfMonths=[31,28,31,30,31,30,31,31,30,31,30,31]
def isLeapYear(year):
	if year%4==0 or year%400==0:
		return True 
	elif year %100==0:
		return False
	else:
		return False
		
