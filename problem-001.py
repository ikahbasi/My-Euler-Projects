# Multiples of 3 and 5
# Find the sum of all the multiples of 3 or 5 below 1000.
a = 0
for i in range(0, 1000):
    if (i%3==0) or (i%5==0):
        a += i
print(a)
