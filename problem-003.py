def is_prime(num):
	for j in range(2, num // 2):
		if not num % j:
			return False
	return True

num = 600851475143
for i in range(2, num // 2):
	if is_prime(i):
		while not num % i:
			num /= i
			if is_prime(int(num)):
				print(num)
				exit()
