#10001st prime
#What is the 10 001st prime number?

from myfunc import pyfunc

def nth_prime_number(th):
	value = 0
	counter = 0
	while counter <= th:
		if pyfunc.isprime(value):
			counter += 1
			prime_value = value
		value += 1
	return prime_value

p = nth_prime_number(10000)
print(p)
