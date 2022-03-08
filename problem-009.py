'''
Special Pythagorean triplet
Problem 9

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a2 + b2 = c2

For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''


def pythagorean(a,b,c):
	if (a**2+b**2)==c**2:
		return True


for c in range(1,500):
	for a in range(1,400):
		for b in range(1,400):
			if pythagorean(a,b,c):
				print a,b,c
				if (a+b+c)==1000:
					f=a*b*c

print 'f is:',f
