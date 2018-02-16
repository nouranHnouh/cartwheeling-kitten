#program that asks the user how many fibonnaci numbers to generate 
#generate them.

def fibonacci():

    count = int(input("How many fibonacci numbers would you like to generate? "))
    i = 1
    if count == 0:
    	#generate empty list
        fibo = []
    elif count == 1:
        fibo = [1]
    elif count == 2:
        fibo = [1,1]

    elif count > 2:
        fibo = [1,1]
        while i < (count-1):
        	#append the list with fibonacci sequence
            fibo.append(fibo[i-1] + fibo[i-2])
            i += 1

    return fibo
print fibonacci()
	










