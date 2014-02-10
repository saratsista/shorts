''' If we list all the natural numbers below 10 that are multiples of 3 or 5, 
we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
'''
#! /usr/bin/python

x = range(0,1000,3) 	# multiples of 3 upto 1000
y = range(0,1000,5)		# multiples of 5 upto 1000
[x.append(i) for i in y if i not in x] #append all values of y not in x to x
print "The sum of multiples of 3 and 5 upto 1000 is {0}".format(sum(x))		
# add all elements of x and return the sum
