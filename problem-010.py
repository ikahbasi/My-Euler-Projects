'''
Summation of primes
Problem 10

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''
from myfunc import pyfunc


sum_prime_number = 0
for num in pyfunc.range_generator(0, 2000000):
	if pyfunc.isprime(num):
		sum_prime_number += num

print(sum_prime_number)
