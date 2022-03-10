from math import sqrt, ceil


def range_generator(start, end, step=1):
    num = start
    while num < end:
        yield num
        num += step

def isprime(num):
    if num in [0, 1]:
        prime = False
    elif num == 2:
        prime = True
    else:
        prime = True
        for j in range_generator(start=2, end=ceil(sqrt(num)+1)):
            if not num % j:
                prime = False
    return prime

def nth_prime_number(th):
	value = 0
	counter = 0
	while counter <= th:
		if isprime(value):
			counter += 1
			prime_value = value
		value += 1
	return prime_value