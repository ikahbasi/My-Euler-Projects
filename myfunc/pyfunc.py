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


def lst_prime(num):
    lst = []
    for ii in range_generator(start=2, end=num+1):
        if isprime(ii):
            lst.append(ii)
    return lst

def prime_factors(num):
    lst_prime_num = lst_prime(num)
    lst_prime_factor = []
    while num != 1:
        for p in lst_prime_num:
            while num%p==0:
                lst_prime_factor.append(p)
                num = num/p
    return lst_prime_factor


def divisors(num):
    lst = [ii for ii in range(1, num+1) if num%ii==0]
    return lst

def gcd(num1, num2):
    # Greatest common divisor  GCD
    div1 = set(divisors(num1))
    div2 = set(divisors(num2))
    return max(div1 & div2)


def lcm(num1, num2):
    # Least Common Multiple    LCM
    return num1*num2 / gcd(num1, num2)