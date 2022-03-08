#Even Fibonacci numbers
#By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
a=[1,2]
b=1
while a[b]<4000000:
	a.append(a[b]+a[b-1])
	b+=1
print 'list of fibonanchi is:\n',a
sum_a=sum(a)
print '\nsum of list fibonanchi is:',sum_a

list_even=[]
for i in a:
	if i%2==0:
		list_even.append(i)
sum_even=sum(list_even)

print '\nlist of even fibonanchi is:\n',list_even
sum_a=sum(a)
print '\nsum of even fibonanchi is:',sum_even

