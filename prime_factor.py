#a procedure that returns the largest prime number 
def largest_prime_factor(n):
	
	i=2
	while i*i<=n:
		if n%i:
			i+=1
		else:
			n=n//i
	return n 

user_input=raw_input("Enter a number:")
print largest_prime_factor(int(user_input)) 