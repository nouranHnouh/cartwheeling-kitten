"""Write a program that computes the net 
amount of a bank account based a transaction log from console input. The transaction log format is shown as following:
D 100
W 200"""

net_amount=0

while True:
	a = raw_input()
	if not a:
		break
	values = a.split(" ")
	operation = values[0]
	amount = int(values[1])
	if operation=="D":
		net_amount+=amount
	elif operation=="W":
		net_amount-=amount
	else:
		pass
print (net_amount)