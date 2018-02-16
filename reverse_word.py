def reverse_word(string):
	first=string.split() # convert string into list
	reverse=first[::-1] #reverse the sentence
	return '  '.join(reverse) #convert them back to string
	
user=raw_input("please Enter a word/s :")
print reverse_word(user)



