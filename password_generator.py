#this program generate a random password
#and ask the user for the length of their password 
#strong password have mix of lowercase letter, uppercase letter
#numbers and symbols
import random 
import string 
#has lowercase alphabet
characters=string.ascii_letters+string.digits+string.punctuation
pw_length=int(raw_input(" How many characters in your password? "))# password length

next_index=random.sample(characters,pw_length)

pwstring=''.join(next_index)  
print pwstring
