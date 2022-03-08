# Problem 1
# Multiples of 3 and 5
# Find the sum of all the multiples of 3 or 5 below 1000.

###################################### solution 1

sum_multiples = 0
for num in range(0, 1000):
    if (num%3==0) or (num%5==0):
        sum_multiples += num
print(sum_multiples)

###################################### solution 2

def range_generator(start, end):
    num = start
    while num < end:
        yield num
        num += 1


sum_multiples = 0
for num in range_generator(0, 1000):
    if (num%3==0) or (num%5==0):
        sum_multiples += num
print(sum_multiples)
