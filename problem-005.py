'''
Smallest multiple
Problem 5

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

from math import sqrt
from myfunc import pyfunc


a = 1
for b in range(1, 21):
    lcm = (a*b) // pyfunc.gcd(a, b)
    a = lcm

print(lcm)
