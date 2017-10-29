def sumofdigit(num):
	num=str(num)
	sum=0
	for i in num:
		sum+=int(i)
	return sum
print sumofdigit('123432')
