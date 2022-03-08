#10001st prime
#What is the 10 001st prime number?
from math import sqrt

def aval(n):
	k=int(sqrt(n)+1)
	avval=True
	
	for i in range(2,k):
		if n%i==0:
			avval=False
			break
	return avval

count=0
i=2
while count<10001:
	if aval(i):	
		#print i ,'is aval'
		count+=1
		b=i
		i+=1
	else:
		i+=1

print 'count of aval number is',count
print b
