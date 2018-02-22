class BankAccount():
	"""class bank account has information about the balance of the account"""
	
	def __init__(self):
		self.balance=0
	def withdraw(self,amount):
		self.balance-=amount
		return self.balance
	def deposit(self,amount):
		self.balance+=amount
		return self.balance
		#inheret from banckAccount 
class MinimumBalanceAccount(BankAccount):
	def __init__(self,minimum_balance):
		BankAccount.__init__(self)
		self.minimum_balance=minimum_balance
	#check if we mainta
	def withdraw(self,amount):
		if self.balance-amount<self.minimum_balance:
			print self.balance 
			print "sorry minimum balance must be maintained"
		else:
			BankAccount.withdraw(self,amount)
a=BankAccount()
b=BankAccount()
print (a.deposit(100))
print (b.deposit(200))
print (b.withdraw(10))
print (a.withdraw(20)) 
minimum_balance=MinimumBalanceAccount(90)
minimum_balance.withdraw(100) 
