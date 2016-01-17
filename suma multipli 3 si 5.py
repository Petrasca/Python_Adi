print "If we list all the natural numbers below 10 that "
print "are multiples of 3 or 5, we get 3 , 5 , 6 and 9."
print "The sum of these multiples is 23."
print "This program will find the sum of all the multiples of 3 or 5 below X. "

print "______________________"
print " "


X = input("Enter the value for \'X\' here: ")
print " "
Sum = 0
i=1

while i < X :
    if i%3==0 or i%5==0:
        Sum = Sum + i
    i +=1

print "The sum of all the multiples of 3 or 5 below " + str(X) + " is " + str(Sum)

print " "
print " "
raw_input ("Press <Enter> to exit.      by adipetrasca@yahoo.com")
