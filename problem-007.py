#10001st prime
#What is the 10 001st prime number?
from math import sqrt

def range_generator_forward(start, end, step=1):
    num = int(start)
    while num < end:
        yield num
        num += step


def prime(num):
    for j in range_generator_forward(start=2, end=sqrt(num)+1):
        if not num % j:
            return False
    return True

def nth_prime_number(th):
	value = 0
	counter = 0
	while counter <= th:
		if prime(value):
			counter += 1
			prime_value = value
		value += 1
	return prime_value

p = nth_prime_number(10001)
print(p)
