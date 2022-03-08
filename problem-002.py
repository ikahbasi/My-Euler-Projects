#Even Fibonacci numbers
#By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.


fibo = [1, 2]
while fibo[-1] < 4000000:
    _next = sum(fibo[-2:])
    fibo.append(_next)
even_fibo = [_ for _ in fibo if _%2==0]
print(sum(even_fibo))
