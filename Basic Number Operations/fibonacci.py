def nth_fibonacci(n):
	if n>0:
		if n==1:
			return 0
		elif n==2:
			return 1
		else:
			f=nth_fibonacci(n-1)+nth_fibonacci(n-2) 
		return f