class Customer():
	"""A customer of TD Bank with an account. customers have the 
	following properties:
	Attributes:
	name: A string of a customer name 
	balamnce: a float of customer`s current balance
	"""
	#intialize constructor 
	def __init__(self,name,balance=0.0):
		self.name=name
		self.balance=balance
	#withdraw method takes an amount as an input 
	#and return the remaining balance after withdraw
	def withdraw(self,amount):
		if self.balance<amount:
			print "I cant give you that amount !"
		else: 
			self.balance-=amount 
		return self.balance 
	#method deposit return the current balance after deposit 
	def deposit(self,amount):
		self.balance+=amount 
		return self.balance 

	def print_info(self):
		print ("\n")
		print ("Welcome "+self.name)
		print ("your current balance is: "+str(self.balance))
		print ("-------------------")

#create an instances 
a=Customer(" Jhon",1000.0)
a.print_info()
print "your balance after withdrawal is: ",a.withdraw(200)
print "your balance after deposit is: " , a.deposit(100)



    		






