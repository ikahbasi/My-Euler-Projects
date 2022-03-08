#Largest palindrome product
#Problem 4 
#Find the largest palindrome made from the product of two 3-digit numbers.
oza=False
g=[]
for a in range(1,1000):
	for b in range(1,1000):
		c=a*b
		d=str(c)
		length=len(d)/2
		if len(d)==6:
			if d[0]==d[-1] and d[1]==d[-2] and d[2]==d[-3]:
				g.append(c)

print(max(g))
