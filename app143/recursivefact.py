def recursive_factorial(n):
	if n==1:
		return n
	else:
		return n*recursive_factorial(n-1)

num=5
if num<0:
	print "factorial is not posible"
elif num==0:
	print "factorial of the Zero is 1"
else:
	print "factorial of the ",num,"is",recursive_factorial(num)
