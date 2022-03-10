'''
Summation of primes
Problem 10

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''
from math import sqrt, ceil


def range_generator_forward(start, end, step=1):
    num = int(start)
    while num < end:
        yield num
        num += step

def prime(num):
	if num == 2:
		return True
	else:
		for j in range_generator_forward(start=2, end=ceil(sqrt(num)+1)):
			if not num % j:
				return False
		return True


sum_prime_number = 0
for num in range_generator_forward(2, 2000000):
	if prime(num):
		sum_prime_number += num

print(sum_prime_number)
