"""Write a program that accepts 
a sequence of whitespace separated words as input 
and prints the words after removing all duplicate words 
and sorting them alphanumerically."""

s=raw_input(" Enter a sequence of words: ")
words=[word for word in s.split(" ")]
print (" ".join(sorted(set(words))))

