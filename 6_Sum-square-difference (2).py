#Sum square difference
#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
num=100
A=[]
ran=range(1,num+1)
for i in ran:
	a=i**2
	A.append(a)
b=sum(A)
print b

sumnum=sum(ran)
sumnum=sumnum**2
print sumnum

print 'ekhtelaf:',sumnum-b
