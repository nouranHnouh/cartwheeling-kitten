class String():
	"""class that takes a string from input and print it"""
	def __init__(self):
		self.string=" "
	def getString(self):
		self.string=raw_input("Enter a string: ")
	
	def printString(self):
		#print strin in uppercase
		print self.string.upper()

#create instances 
a=String()
a.getString()
a.printString()


