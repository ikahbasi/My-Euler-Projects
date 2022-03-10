"""
Largest prime factor
Problem 3
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""

from numpy import sqrt
from myfunc import pyfunc


lst = []
num = 600851475143
for i in pyfunc.range_generator(start=2, end=sqrt(num)):
    if pyfunc.isprime(i) and (num%i)==0:
        lst.append(i)
print(max(lst))
