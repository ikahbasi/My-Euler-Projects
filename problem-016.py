'''
Power digit sum
Problem 16
215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
What is the sum of the digits of the number 21000?
'''

num = str(2 ** 1000)

_sum = 0
for ii in num:
	_sum += int(ii)

print(_sum)