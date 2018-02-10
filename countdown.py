# Define a procedure, countdown, that takes a
# positive whole number as its input, and prints
# out a countdown from that number to 1,
# followed by Blastoff!

def countdown(n):
    if n>0:
        i=n
        while i:
            print i
            i=i-1
    print 'Blastoff!'




countdown(3)
#>>> 3
#>>> 2
#>>> 1
#>>> Blastoff!
