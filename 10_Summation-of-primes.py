'''
Summation of primes
Problem 10

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''
from math import sqrt
c=[]
for a in range(2,2000000):
	p=int(sqrt(a))+1
	L=True
	print a,p
	for b in range(2,p):
		if a%b==0:
			L=False
			break
	if L:
		c.append(a)
#print c
print 'sum of c is:',sum(c)
