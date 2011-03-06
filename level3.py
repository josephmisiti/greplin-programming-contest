#!/usr/bin/python

import sys
primes_under_100 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

def isprime(n):
	if n <= 100:
		return n in primes_under_100
	if n % 2 == 0 or n % 3 == 0:
		return False

	for f in range(5, int(n ** .5), 6):
		if n % f == 0 or n % (f + 2) == 0:
			return False
	return True


def fib(num):
	if num==0 or num==1:
		return num
	else:
		return fib(num-1)+fib(num-2)

def findnum(num):
	# find start of fib serie
	ii = 0
	while fib(ii) <= num:
		ii +=1
	fibstart = ii
	found = True

	while found:
		test = fib(fibstart)
		print "testing: ", test
		if isprime(test):
			found = False
			break
		fibstart+=1
			
	print fib(fibstart)
	# now try to determine if its prime
	
	

def main(p):
	p = int(p)
	findnum(p)
	
	
if __name__ == "__main__":
	main(sys.argv[1])