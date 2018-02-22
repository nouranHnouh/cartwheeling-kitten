"""factorial functions returns the factorial of number """
def factorial (n):
	if n==0:
		return 1
	else:
		return n*factorial(n-1)

x=int(raw_input("Enter a Number : "))
print factorial(8)