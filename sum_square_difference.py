#difference between the sum of the squares of the first one hundred 
#natural numbers and the square of the sum.
sumsquare=0
sum=0
for i in range(1,101):
	sum+=i
	sumsquare+=i**2
	difference= sum**2-sumsquare
print (difference)