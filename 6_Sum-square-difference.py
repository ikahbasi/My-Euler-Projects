#Largest prime factor
#What is the largest prime factor of the number 600851475143
from math import sqrt
num=600851475143

p=sqrt(num)
#print 'sqrt:',p
p=int(p)
#print 'int:',p

aval=[]
for i in range(1,p):
	avval=True
	for b in range(2,i):
		if i%b==0:
			avval=False
			break
	if avval==True:
		aval.append(i)
		#print i,' is append to aval list'
aval.reverse()
prime_number=aval
#print 'prime_number:',prime_number

A=1


for i in prime_number:
	if num%i==0:
		A=A*i
		print 'prime number is:',i
print 'A:',A

