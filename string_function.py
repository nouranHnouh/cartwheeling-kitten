# Define a procedure, is_friend, that
# takes a string as its input, and
# returns a Boolean indicating if
# the input string is the name of
# a friend.# and return True if the friend name start with 'D' or 'N'
#otherwise return false
def is_friend(s):
	if s[0]=='D' or s[0]=='N':
		return True
	else:
		return False
		








# test the function 

print is_friend('Diane')
#>>> True

print is_friend('Naomy')
#>>> False
print is_friend('Fred')
