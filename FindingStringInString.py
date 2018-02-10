#find string in string using find()
pythagoras = 'There is geometry in the humming of the strings, there is music in the spacing of the sphere.'
print pythagoras.find('strings') 
print pythagoras [40: ]
print pythagoras.find('T')
print pythagoras [0:1]
print pythagoras.find('sphere')
s= "any string"
print s.find(s) 
print 's'.find('s')
print s.find ('')
print s.find (s+'!!!')+1


# Use the string.find method to locate "NOUN" and "VERB" in the string text
# and store those positions in the variables noun_position and verb_position respectively.

text = """Wow this is a fairly long body of text. Quite a few characters too.
I wonder if the string.find method could help find where NOUN is located.
That way, I could go out and VERB with my friends rather than counting characters
all day long!"""

noun_position = text.find('NOUN')
verb_position = text.find('VERB')
print noun_position
print verb_position
