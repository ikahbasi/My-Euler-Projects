"""
Largest prime factor
Problem 3
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""

import numpy as np

def range_generator_forward(start, end, step=1):
    num = int(start)
    while num < end:
        yield num
        num += step


def range_generator_backward(start, end, step=-1):
    num = int(start)
    while num > end:
        yield num
        num += step


def prime(num):
    for j in range_generator_forward(start=2, end=np.sqrt(num)):
        if not num % j:
            return False
    return True


num = 600851475143
lst = []
for i in range_generator_forward(start=2, end=np.sqrt(num)):
    if prime(i) and (num%i)==0:
        print(1, i)
        if (i**2) > (num/2):
            print(2, i)
            break
        lst.append(i)
print(max(lst))
