#reverse is a function that reverse the string. 
#it take string as input and return its reverse
def reverse(s):
	return s[::-1] 


#function palindrom check if the string is palindrome(string that reads the same forward and backward)
def palindrome_string(c):
	rev=reverse(c)
	if c==rev:
		return True
	return False

	#test the code
	#ask the user to enter a string
string=raw_input("Please Enter string:")
print palindrome_string(string)


	
		
